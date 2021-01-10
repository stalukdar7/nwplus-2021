import requests

import json

response = json.loads(requests.get("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events").text)

print (response)
