from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
Soup = BeautifulSoup(html, 'lxml')

items = Soup.find_all('span')
li = list()
for i in items :
   i = str(i)
   a = re.findall('[0-9]+', i)
   li.append(int(a[0]))
print(sum(li))