import requests
from urllib.parse import urlparse
from .modules.headers import check_headers
from .modules.https_check import check_https
from .modules.xss import test_xss
from .modules.sqli import test_sqli
from .utils.risk import calculate_risk

def run_scan(target):
    if not target.startswith("http"):
        target = "http://" + target

    parsed = urlparse(target)
    if not parsed.netloc:
        return {"error": "Invalid URL"}

    try:
        requests.get(target, timeout=5)
    except:
        return {"error": "Target not reachable"}

    results = []
    results += check_headers(target)
    results += check_https(target)
    results += test_xss(target)
    results += test_sqli(target)

    risk = calculate_risk(results)

    return {
        "target": target,
        "issues": results,
        "risk": risk
    }
