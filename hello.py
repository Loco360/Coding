import requests

r = requests.get("https://coreymy.com")
print(r.status_code)
print(r.ok)

