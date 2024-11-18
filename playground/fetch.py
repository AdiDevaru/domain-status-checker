import asyncio
import aiohttp
import requests
import cloudscraper
from bs4 import BeautifulSoup  

from geventhttpclient import HTTPClient
from geventhttpclient.url import URL

error_keywords = ["404", "not found", "this page does not exist", "page not found", "error"]    
headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0.0.0 Safari/537.36 (compatible; DomainStatusChecker/1.0)'
    }
timeout = 30

def domain_status_check(domain):
    
    try:
        parsed_url = URL(domain)
        client = HTTPClient(parsed_url.host, port=parsed_url.port or 443, ssl=parsed_url.scheme == 'https', concurrency=10)
        response = client.get(parsed_url.request_uri, headers=headers)
        
        status_code = response.status_code
        content = response.read()
        client.close()

        # Parse HTML content for error keywords
        soup = BeautifulSoup(content, "html.parser")
        page_title = soup.title.string.strip() if soup.title and soup.title.string else ""

        if any(keyword.lower() in page_title.lower() for keyword in error_keywords):
            return domain, 404

        return domain, status_code

    except Exception as e:
        # print("EXCEPTION")
        return domain, None
    
    # try:
    #     response = requests.get(domain, headers=headers, timeout=timeout)
    #     status_code = response.status_code
    #     content = response.text
        
    #     soup = BeautifulSoup(content, "html.parser")
    #     page_title = soup.title.string.strip() if soup.title and soup.title.string else ""
        
    #     if any(keyword.lower() in page_title.lower() for keyword in error_keywords):
    #         return domain, 404
        
    #     return domain, status_code
    
    # except requests.exceptions.Timeout: return domain, 408
    # except requests.exceptions.ConnectionError: return domain, 503
    # except requests.exceptions.SSLError: return domain, 526
    # # except requests.exceptions.ClientResponseError as e: return e.status
    # except Exception: return domain, None

async def async_domain_status_check(session, domain, max_redirects=5):    
    try:
        async with session.get(domain, headers=headers, timeout=timeout, allow_redirects=True) as response:
            status_code = response.status
            
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            
            page_title = soup.title.string.strip() if soup.title and soup.title.string else ""
            
            # return {"message": "Error page not found", "domain": domain, "status": 404}
            if any(keyword.lower() in page_title.lower() for keyword in error_keywords): return domain, 404
                
            return domain, status_code
            
    except asyncio.TimeoutError: return domain, 408
    except aiohttp.ClientConnectionError: return domain, 503
    except aiohttp.ClientSSLError: return domain, 526
    except aiohttp.ClientResponseError as e: return domain, e.status
    except aiohttp.TooManyRedirects: return domain, None
    except Exception: return domain, None

    
    
    
        
