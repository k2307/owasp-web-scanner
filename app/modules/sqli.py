import requests

def test_sqli(url):
    issues = []
    payload = "' OR '1'='1"
    try:
        r = requests.get(url, params={"id": payload}, timeout=5)
        if "sql" in r.text.lower() or "error" in r.text.lower():
            issues.append({
                "type": "Possible SQL Injection",
                "category": "A03: Injection",
                "detail": "SQL error message detected",
                "severity": "High"
            })
    except:
        pass
    return issues
