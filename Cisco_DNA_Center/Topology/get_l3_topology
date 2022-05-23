import os
import requests
import json
from rich import print

token = os.getenv("TOKEN")
url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/topology/l3/OSPF"
parameters = {'X-Auth-Token': token}

def topology_l3(url):
        get_request = requests.get(url, verify=False, headers=parameters)
        response = get_request.json()
        print(response)

topology_l3(url)