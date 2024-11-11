import requests
import cloudscraper
from bs4 import BeautifulSoup  

def domain_status_check(domain):
    error_keywords = ["404", "not found", "this page does not exist", "page not found", "error"]    
    headers = {
        "User-Agent": 'Mozilla/5.0 (compatible; DomainStatusChecker/1.0)'
    }
    timeout = 60
    
    try:
        response = requests.get(domain, headers=headers, timeout=timeout)
        status_code = response.status_code
        
        # Logic to fetch 404 error from page title
        soup = BeautifulSoup(response.content, 'html.parser')
        page_title = (soup.title).string.strip() if soup.title is not None else ""
        # print(page_title)
        
        if any(keyword.lower() in page_title.lower() for keyword in error_keywords):
            return {"message": "Error page not found", "domain": domain, "status": 404}
        
        if status_code == 200: return {"message": "Success", "domain": domain, "status": f'{response.status_code}'}
        
        # Logic to implement cloudscraper
        scraper = cloudscraper.create_scraper() 
        try: 
            scraper_response = scraper.get(domain, headers=headers, timeout=timeout)
            
            if status_code == 200: return {"message": "Success", "domain": domain, "status": f'{scraper_response.status_code}'}
            
            return {"message": "Failed", "domain": domain, "status": f'{scraper_response.status_code}'}
        
        except Exception as e:
            return {"message": f"Unexpected error: {e}", "domain": domain, "status": "-"}

    # Request timed out
    except requests.exceptions.Timeout as e: return {"message": "Timeout Error - Request timed out", "domain": domain, "status": 408}

    # Network-related error
    except requests.exceptions.ConnectionError: return {"message": "Connection error", "domain": domain, "status": 503}

    # SSL certificate error
    except requests.exceptions.SSLError: return {"message": "SSL certificate error", "domain": domain, "status": 526}

    # HTTP error 
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response else 500
        return {"message": "HTTP error", "domain": domain, "status": status_code}

    # Too many redirects
    except requests.exceptions.TooManyRedirects: return {"message": "Too many redirects", "domain": domain, "status": 310}

    # General request exception
    except requests.exceptions.RequestException as e:
        # status_code = 500  
        if hasattr(e, 'response') and e.response is not None:
            status_code = e.response.status_code
        return {"message": "An unknown error occurred: {e}", "domain": domain, "status": status_code}

    # Any other unhandled exception
    except Exception as e: return {"message": f"Unexpected error: {e}", "domain": domain, "status": "-"}

    
