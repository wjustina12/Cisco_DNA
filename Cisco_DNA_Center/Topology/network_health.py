import os
import json 
import requests 
from rich import print

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-health"
token = os.getenv("TOKEN")
header = {'X-Auth-Token' : token}

def network_health(url):
    get_request = requests.get(url, verify=False, headers=header)
    response = get_request.json()
    print(response)

network_health(url)

