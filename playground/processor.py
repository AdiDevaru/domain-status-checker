from concurrent.futures import ThreadPoolExecutor
from .checker import domain_status_check

def domain_check_parallel(domains, max_workers=20):
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        try:
            results = executor.map(domain_status_check, domains)
        except Exception as e:
            results.append({"message": f"Thread Pool Error: {e}", "status_code": 500}) 
        finally:
            return results