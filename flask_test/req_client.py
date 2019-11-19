import requests

response = requests.post(url='http://127.0.0.1:5000/')
print('status_code: ', response.status_code)
print('content: ', response.content.decode())
print('text: ', response.text)
print(type(response.json()))