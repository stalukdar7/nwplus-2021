import requests

import json

response = json.loads(requests.get("https://eonet.sci.gsfc.nasa.gov/api/v3/events").text)

print (response)
