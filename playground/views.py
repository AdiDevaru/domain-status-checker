# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .processor import fetch_domains
from .models import InitialUrls, FinalUrls
# from .tasks import fetch_status_codes, check_domains_task

# Create your views here.
class DomainStatus(APIView):
    def post(self, request, *args, **kwargs):
        domains = request.data.get("domains", [])
        try:
            results = fetch_domains(domains)
            # print(check_domains_task.delay(domains))
        except Exception as e:
            return Response({"error": f"Internal server error: {str(e)}"}, status=500)
        return Response(results, status=200)

class InsertUrls(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        scan_id = 2
        domains = request.data.get("domains", [])
        if not isinstance(domains, list) or not domains:
            return Response(
                {"error": "Invalid input. Expected a list of URLs under 'domains'"},
                status=400
            )
            
        initial_urls_data = [
            InitialUrls(scan_id=scan_id, url=url) for url in domains
        ]
        
        InitialUrls.objects.bulk_create(initial_urls_data)
        
        # fetch_status_codes.delay()
        
        return Response(
            {"message": "URLs successfully inserted. Scraping pending..."},
            status=202
        )


        