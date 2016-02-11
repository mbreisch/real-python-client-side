import requests

# retrieve the webpage
r= requests.get("http://www.python.org")
print r.content