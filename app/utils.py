import requests

def send(url, data, token=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'    
    try:
        res = requests.post(url, json=data, headers=headers, timeout=5)
        return res.status_code
    except:
        return None

