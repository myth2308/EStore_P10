

# import json
# import urllib.request

# url = urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google")
# data = json.loads(url.read().decode())

# appliction/json
# text/jon

import requests
import json

url_api = 'https://fakestoreapi.com/products/1/'
# data = requests.get(url_api)
# data = json.loads(requests.get(url_api)) # Cach 1
data = requests.get(url_api).json() #Cach 2
print(data)