import json
import ssl
from urllib.request import DataHandler, urlopen
import urllib.parse , urllib.error

api_key = 42
serviceurl="http://py4e-data.dr-chuck.net/json?"


#Ignore SSL certificates 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#read the name of the place
place = input("Enter the name of the place ")

#clear a dict and read addresses and keys
parms = dict()
parms['address'] = place
parms['key'] = api_key

#clear an url to recieve Json
url = serviceurl + urllib.parse.urlencode(parms)
#print(url)
uh = urlopen(url, context=ctx)
data = uh.read().decode()

#parse json
js = json.loads(data)

#error check
if not js or 'status' not in js or js['status'] != 'OK':
    print('failed to retrieve data')

#read latitude, logitude and place id from the json
lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
place_id = js['results'][0]['place_id']
zip_code = js['results'][0]['address_components'][-1]['long_name']
print("The co ordinates of the ",place, " are ","Latitude =",lat,"Longitude =",lng)
print("Zip code of ", place, 'is', zip_code)
print("The id of  ", place," is ", place_id)
