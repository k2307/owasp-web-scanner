import requests

def check_headers(url):
    issues = []
    r = requests.get(url)
    headers = r.headers

    required = ['X-Frame-Options', 'Content-Security-Policy', 'Strict-Transport-Security']
    for h in required:
        if h not in headers:
            issues.append({
                "type": "Missing Security Header",
                "category": "A05: Security Misconfiguration",
                "detail": f"{h} header missing",
                "severity": "Medium"
            })
    return issues
