#!/usr/bin/env python

import requests
import json


api_token = 'qm1SSKPqmNyo9OMVcgf05MxGGsG04hZGnOKEk2ED'
api_url_base =  'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'
#api_url_base = 'https://api.digitalocean.com/v2/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

data = get_account_info()
print(data)
