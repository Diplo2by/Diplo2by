from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as et

#Ignore SSL certificates 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#read url from the user and extract xml
url = input("Enter the URL-")
xml = urlopen(url, context=ctx).read()

#parse xml
tree = et.fromstring(xml)

lst = list()
counts = tree.findall('comments/comment')

#look for data by iterating through elements
for child in counts:
    a = child.find('count').text
    lst.append(int(a))
print(sum(lst))    