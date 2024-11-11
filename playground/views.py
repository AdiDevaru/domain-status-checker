# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .processor import run_domain_check
from .serializers import DomainSerializer

# Create your views here.
class DomainStatus(APIView):
    def post(self, request):
        domains = request.data.get("domains", [])
        try:
            results = run_domain_check(domains)
            serializer = DomainSerializer(results, many=True)
        except Exception as e:
            return Response({"error": f"Internal server error: {str(e)}"}, status=500)
        return Response(serializer.data, status=200)
        