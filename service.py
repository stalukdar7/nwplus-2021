import requests

import json

data = json.loads(requests.get("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events").text)

def func(lat, long, event, rad, time):
    
       
