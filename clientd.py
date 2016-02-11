# submit form get full response back
import requests

url="http://httpbin.org/post"
data={'fname':'Matt','lname':'Reisch'}

r=requests.post(url,data=data)

print r.content