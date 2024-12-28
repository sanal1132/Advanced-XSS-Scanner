import requests

def test_payloads(url, parameters, input_fields, payloads):
    results = []
    for payload in payloads:
        for param in parameters:
            crafted_url = f"{url}?{param}={payload}"
            response = requests.get(crafted_url)
            if payload in response.text:
                results.append({"parameter": param, "payload": payload, "url": crafted_url})
        for field in input_fields:
            # Placeholder for field testing logic
            results.append({"field": field, "payload": payload, "url": url})
    return results
