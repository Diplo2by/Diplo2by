from urllib.request import urlopen
import json
import ssl

#Ignore SSL certificates 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Read the data
url = input("Enter the URL-")
data = urlopen(url, context=ctx).read()

#parse JSON
info = json.loads(data)
lst = list()
items = info.get('comments')

#read the count
for item in items:
    a = item['count']
    #make a list of counts
    lst.append(a)
print(sum(lst))