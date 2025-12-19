def classify_attack(payload):
    payload = payload.lower()

    if "or 1=1" in payload or "'" in payload:
        return "SQL Injection"
    elif "<script>" in payload:
        return "XSS"
    elif "wget" in payload or "curl" in payload:
        return "Malware Download"
    else:
        return "Unknown / Credential Stuffing"
