def check_https(url):
    issues = []
    if url.startswith("http://"):
        issues.append({
            "type": "No HTTPS",
            "category": "A02: Cryptographic Failures",
            "detail": "Site does not use HTTPS",
            "severity": "High"
        })
    return issues
