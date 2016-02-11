import requests

r=requests.get("http://www.python.org")

# write page to file
with open("test_requests.html","wb") as code:
    code.write(r.content)