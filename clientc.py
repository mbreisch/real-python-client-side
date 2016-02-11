# submitting a web form

import requests

url = 'http://httpbin.org/post'
data = {'fname': 'Matthew', 'lname': 'Reisch'}

r=requests.post(url,data=data)

print r
