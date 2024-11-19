# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .processor import run_domain_check
# , run_domain_check
from .models import InitialUrls, FinalUrls
from .tasks import fetch_domains, fetch_status_codes
# from .tasks import fetch_status_codes, check_domains_task

# Create your views here.
class DomainStatus(APIView):
    def post(self, request, *args, **kwargs):
        domains = request.data.get("domains", [])
        try:
            # task = fetch_domains.delay(domains, pool_size=100)
            results = run_domain_check(domains)
            # results = fetch_domains(domains, pool_size=100)
            # return Response({"status": "Pending"}, status=200)
            # results = run_domain_check(domains)
            # print(check_domains_task.delay(domains))
        except Exception as e:
            return Response({"error": f"Internal server error: {str(e)}"}, status=500)
        return Response(results, status=200)

class InsertUrls(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):        
        domains = request.data
        if not isinstance(domains, list) or not domains:
            return Response(
                {"error": "Invalid input. Expected a list of URLs under 'domains'"},
                status=400
            )
            
        initial_urls_data = []
        
        for domain in domains:
            scan_id = domain.get("scan_id")
            link_url = domain.get("link_url")
            
            if not scan_id or not link_url:
                return Response(
                    {"error": "Each entry must contain 'scan_id' and 'link_url'"},
                    status=400
                )
            
            initial_urls_data.append(InitialUrls(scan_id=scan_id, url=link_url))
        
        InitialUrls.objects.bulk_create(initial_urls_data)
        
        fetch_status_codes.delay([domain['link_url'] for domain in domains])
        
        return Response(
            {"message": "URLs successfully inserted. Scraping initiated"},
            status=202
        )


        