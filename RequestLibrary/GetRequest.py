import requests

url = 'https://postman-echo.com/get'
params = {'somekey': 'somevalue'}

x = requests.get(url, params)

print(x.text)
