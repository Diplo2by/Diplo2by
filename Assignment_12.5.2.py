from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificates 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Prompt for url to follow
url = input('Enter url - ')
pos = int(input("Enter the position "))
t= int(input("Enter the number of times "))

#process the input link
html = urlopen(url, context=ctx).read()
Soup = BeautifulSoup(html, 'lxml')

i = 0
#loop through the link 
while i < t:
    tags = Soup('a')
    tag = tags[pos-1]
    link = tag.get('href',None)
    print(link)
    #make url as link to click the particular(irl)
    url = link
    html = urlopen(url, context=ctx).read()
    Soup = BeautifulSoup(html, 'lxml')
    i+=1
