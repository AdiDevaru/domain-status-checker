from gevent import monkey, spawn, joinall
monkey.patch_all()

import asyncio
import aiohttp

from .fetch import async_domain_status_check, domain_status_check

def fetch_domains(domains, batch_size=100):
    
    results = []
    for i in range(0, len(domains), batch_size):
        batch = domains[i:i + batch_size]
        jobs = [spawn(domain_status_check, domain) for domain in batch]
        joinall(jobs)
        results.extend(job.value for job in jobs)
    return results

# async def domain_check_parallel(domains):
#     # tasks = [async_domain_status_check(url) for url in domains]
#     # return await asyncio.gather(*tasks)
    
#     connector = aiohttp.TCPConnector(limit_per_host=100)
#     async with aiohttp.ClientSession() as session:

#         tasks = [asyncio.create_task(async_domain_status_check(session, url)) for url in domains]
#         return await asyncio.gather(*tasks)

def run_domain_check(domains, batch_size=100):
    # return asyncio.run(domain_check_parallel(domains))
    return fetch_domains(domains, batch_size)
    
