# from gevent import monkey, spawn, joinall
# monkey.patch_all()
from gevent.pool import Pool


from celery import shared_task
from rest_framework.response import Response

import requests

from .processor import run_domain_check
from .models import InitialUrls, FinalUrls
from .fetch import domain_status_check

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0.0.0 Safari/537.36 (compatible; DomainStatusChecker/1.0)"
# }

# @shared_task
# def check_domains_task(domains):
#     """Celery task to check domains."""
#     return run_domain_check(domains)

@shared_task
def fetch_domains(domains, pool_size=100):
    
    results = run_domain_check(domains)
    return results
    
    # session = requests.Session()
    # session.headers.update(headers)
    # return f"Processed {len(domains)} domains with pool size {pool_size}"
    # pool = Pool(pool_size)
    
    # jobs = [pool.spawn(domain_status_check, domain) for domain in domains]
    # pool.join()
    # results = [job.value for job in jobs]
    # return results
    

@shared_task
def fetch_status_codes(domains):
    urls = InitialUrls.objects.filter(flag=0)

    if not urls:
        return "No URLs to process"
    
    results = run_domain_check(domains)
    
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

    return {"message": "Status codes fetched and saved"}