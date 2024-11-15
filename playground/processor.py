import asyncio
import aiohttp

from .fetch import async_domain_status_check

async def domain_check_parallel(domains):
    # tasks = [async_domain_status_check(url) for url in domains]
    # return await asyncio.gather(*tasks)
    
    connector = aiohttp.TCPConnector(limit_per_host=100)
    async with aiohttp.ClientSession() as session:

        tasks = [asyncio.create_task(async_domain_status_check(session, url)) for url in domains]
        return await asyncio.gather(*tasks)

def run_domain_check(domains):
    return asyncio.run(domain_check_parallel(domains))
    
