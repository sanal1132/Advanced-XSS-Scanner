def encode_payload(payload, encode_type):
    if encode_type == "html":
        html_entities = {
            "<": "&lt;",
            ">": "&gt;",
            "\"": "&quot;",
            "'": "&#x27;",
            "&": "&amp;",
        }
        for char, entity in html_entities.items():
            payload = payload.replace(char, entity)
        return payload
    elif encode_type == "url":
        from urllib.parse import quote
        return quote(payload)
    elif encode_type == "base64":
        import base64
        return base64.b64encode(payload.encode()).decode()
    return payload
