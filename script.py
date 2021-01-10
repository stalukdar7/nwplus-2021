import requests

import webbrowser

import json

import cgi

form = cgi.FieldStorage()

lattitude = form.getvalue("lattitude")

response = json.loads(requests.get("https://eonet.sci.gsfc.nasa.gov/api/v3/events").text)

webbrowser.open('http://example.com')

print (lattitude)
