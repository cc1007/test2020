import requests

def send_requets(url,method,data,headers)
    if method.upper()="POST"
        res = requets.post(url,data,headers)
        print(res)
