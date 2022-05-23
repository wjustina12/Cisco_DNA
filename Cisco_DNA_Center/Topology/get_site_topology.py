import json
import os 
import requests 
from rich import print 

token = os.getenv("TOKEN")
url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/topology/site-topology'
header = {'X-Auth-Token' : token}

def site_show(url):
    get_request = requests.get(url, verify=False, headers=header)
    response = get_request.json()
    print(response)

site_show(url)