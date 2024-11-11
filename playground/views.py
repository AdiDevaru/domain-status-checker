# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .processor import run_domain_check
from .serializers import DomainSerializer, InitialURLsSerializer
from .models import InitialUrls

# Create your views here.
class DomainStatus(APIView):
    def post(self, request):
        domains = request.data.get("domains", [])
        try:
            results = run_domain_check(domains)
        # serializer = DomainSerializer(results, many=True)
        except Exception as e:
            return Response({"error": f"Internal server error: {str(e)}"}, status=500)
        return Response(results, status=200)

class InsertUrls(viewsets.ModelViewSet):
    
    queryset = InitialUrls.objects.all()
    serializer_class = InitialURLsSerializer
    
    def create(self, request, *args, **kwargs):
        scan_id = 2
        url_list = request.data.get("domains", [])
        if not isinstance(url_list, list) or not url_list:
            return Response(
                {"error": "Invalid input. Expected a list of URLs under 'domains'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        initial_urls_data = [
            InitialUrls(scan_id=scan_id, url=url, flag=0) for url in url_list
        ]
        
        InitialUrls.objects.bulk_create(initial_urls_data)
        
        return Response(
            {"message": "URLs successfully created."},
            status=status.HTTP_201_CREATED
        )