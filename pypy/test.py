import requests

a = 256
url = "http://127.0.0.1:8080/ip/get"

for i in range(300, 600):
    a = i
    data = {
        "token": "sBtwBL5aqu8WNgUhgCv9doPqT",
        "organization": "ic110",
        "mail": str(a) + "@yundun.com"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = requests.post(url, data=data, headers=headers)
    print(res.text, res.status_code)
