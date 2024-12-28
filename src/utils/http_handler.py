import requests

def send_request(url):
    try:
        return requests.get(url)
    except Exception as e:
        print(f"Error sending request: {e}")
        return None
