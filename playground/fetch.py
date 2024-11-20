import asyncio
import aiohttp
import requests
# import cloudscraper
from bs4 import BeautifulSoup  

from requests.exceptions import SSLError

from fake_useragent import UserAgent

# from geventhttpclient import HTTPClient
# from geventhttpclient.url import URL

ua = UserAgent(browsers=["chrome", "edge", "firefox", "safari"])

error_keywords = ["404", "not found", "this page does not exist", "page not found", "error"]    
# headers = {
#         "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0.0.0 Safari/537.36 (compatible; DomainStatusChecker/1.0)'
#     }

timeout = 30

headers = {
        'User-Agent': None,
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer':'https://www.google.com',
        'Priority':'u=0, i',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'none',
        'Sec-Fetch-User':'?1'
    }

def domain_status_check(domain):
    
    try:
        user_agent = ua.random
        headers['User-Agent'] = user_agent
        response = requests.get(domain, headers=headers, timeout=timeout)
        status_code = response.status_code
        content = response.text

        # Parse HTML to check the title for error keywords
        soup = BeautifulSoup(content, "html.parser")
        page_title = soup.title.string.strip() if soup.title and soup.title.string else ""

        # If error keywords are found in the title, return domain,  status as 404
        if any(keyword.lower() in page_title.lower() for keyword in error_keywords):
            return domain,  404

        return domain,  status_code

    except requests.Timeout: return domain,  408 
    except requests.ConnectionError: return domain,  503  
    except SSLError: return domain,  526  
    
    except requests.RequestException as e:
        if hasattr(e.response, 'status_code'):
            return domain,  e.response.status_code
        return domain,  None  

    except Exception: return domain,  None
    
    # try:
    #     url = URL(domain)
    #     client = HTTPClient.from_url(url, concurrency=10, connection_timeout=timeout)
    #     response = client.get(url.request_uri, headers=headers)
        
    #     status_code = response.status_code
    #     content = response.read()
    #     client.close()

    #     soup = BeautifulSoup(content, "html.parser")
    #     page_title = soup.title.string.strip() if soup.title and soup.title.string else ""

    #     if any(keyword.lower() in page_title.lower() for keyword in error_keywords):
    #         return domain,  404

    #     return domain,  status_code

    # except Exception as e:
    #     return domain,  None

async def async_domain_status_check(session, domain):    
    try:
        user_agent = ua.random
        headers['User-Agent'] = user_agent
        
        async with session.get(domain, headers=headers, timeout=timeout, allow_redirects=True) as response:
            status_code = response.status
            
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            
            page_title = soup.title.string.strip() if soup.title and soup.title.string else ""
            
            # return domain,  {"message": "Error page not found", "domain": domain, "status": 404}
            if any(keyword.lower() in page_title.lower() for keyword in error_keywords): return 404
                
            return status_code
            
    except asyncio.TimeoutError: return 408
    except aiohttp.ClientConnectionError: return 503
    except aiohttp.ClientSSLError: return 526
    except aiohttp.ClientResponseError as e: return e.status
    except aiohttp.TooManyRedirects: return None
    except Exception: return None

    
    
    
        
