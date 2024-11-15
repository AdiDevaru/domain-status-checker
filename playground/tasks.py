from celery import shared_task
from rest_framework.response import Response

from .models import InitialUrls, FinalUrls
from .processor import run_domain_check

@shared_task
def fetch_status_codes():
    urls = InitialUrls.objects.filter(flag=0)

    if not urls:
        return "No URLs to process"
    
    domains = [url_obj.url for url_obj in urls]
    results = run_domain_check(domains)
    
    # Create FinalUrls entries in bulk
    status_data = [
        FinalUrls(
            scan_id=url_obj.scan_id,
            url=url_obj.url,
            status=status_code
        )
        for url_obj, status_code in zip(urls, results)
    ]
    FinalUrls.objects.bulk_create(status_data)
    
    InitialUrls.objects.filter(id__in=[url_obj.id for url_obj in urls]).update(flag=1)

    return Response({"message": "Status codes fetched and saved"})