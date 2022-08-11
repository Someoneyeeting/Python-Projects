import requests as req
print("\n\n\n\n\n")
resp = req.request(method='GET', url="https://translate.google.com/?sl=en&tl=ar&text=hello&op=translate")
print("\n\n")
print(resp.text)