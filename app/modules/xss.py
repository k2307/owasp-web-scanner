import requests

def test_xss(url):
    issues = []
    payload = "<script>alert(1)</script>"
    try:
        r = requests.get(url, params={"test": payload}, timeout=5)
        if payload in r.text:
            issues.append({
                "type": "Reflected XSS",
                "category": "A03: Injection",
                "detail": "Payload reflected in response",
                "severity": "High"
            })
    except:
        pass
    return issues
