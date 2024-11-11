from concurrent.futures import ThreadPoolExecutor
from .fetch import async_domain_status_check

import asyncio
import aiohttp

async def domain_check_parallel(domains):
    tasks = [async_domain_status_check(url) for url in domains]
    return await asyncio.gather(*tasks)

def run_domain_check(domains):
    return asyncio.run(domain_check_parallel(domains))

# def domain_check_parallel(domains, max_workers=20):
#     results = []
    
#     with ThreadPoolExecutor(max_workers=max_workers) as executor:
#         try:
#             results = executor.map(domain_status_check, domains)
#         except Exception as e:
#             results.append({"message": f"Thread Pool Error: {e}", "status_code": 500}) 
#         finally:
#             return results
