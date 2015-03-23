import requests, json


url = 'http://192.168.1.208:5000/8x8/'

data = {'iconFile' : 'icon_bang.bmp', 'gridNumber' : 1}
print data
r = requests.put(url, data)

print r.json