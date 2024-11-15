import asyncio
import aiohttp
import requests
import cloudscraper
from bs4 import BeautifulSoup  

error_keywords = ["404", "not found", "this page does not exist", "page not found", "error"]    
headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0.0.0 Safari/537.36 (compatible; DomainStatusChecker/1.0)'
    }
timeout = 60

async def async_domain_status_check(session, domain, max_redirects=5):    
    try:
        # async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(domain, headers=headers, timeout=timeout, allow_redirects=True) as response:
            status_code = response.status
            
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            
            page_title = soup.title.string.strip() if soup.title and soup.title.string else ""
            
            # return {"message": "Error page not found", "domain": domain, "status": 404}
            if any(keyword.lower() in page_title.lower() for keyword in error_keywords): return 404
                
            return status_code
            
    except asyncio.TimeoutError: return 408
    except aiohttp.ClientConnectionError: return 503
    except aiohttp.ClientSSLError: return 526
    except aiohttp.ClientResponseError as e: return e.status
    except aiohttp.TooManyRedirects: return None
    except Exception: return None
    
    try:
        scraper = cloudscraper.create_scraper()
        # print('TEST')
        scraper_response = scraper.get(domain, headers=headers, timeout=timeout)
        # print(scraper_response.status_code)
        return scraper_response.status_code
    except Exception: return None
    
    
    
        
