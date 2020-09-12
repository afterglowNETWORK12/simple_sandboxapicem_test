#Print host from sandboxapicem

import requests
import json
from tabulate import *
from my_apic_em_functions import *


api_url = "https://sandboxapicem.cisco.com/api/v1/host"
ticket = get_ticket()
headers = {
    "content-type": "application/json",
    "X-Auth-Token": ticket
}
resp = requests.get(api_url, headers=headers, verify=False)
print("Status of /host request: ", resp.status_code)
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)
response_json = resp.json()
host_list = []
i = 0
for item in response_json["response"]:
    i += 1
    host = [
            i, 
            item["hostType"], 
            item["hostIp"] 
           ]
    host_list.append( host )

table_header = [
                "Number",
                "Type",
                "IP"
               ]
print( tabulate(host_list, table_header) )

'''
OUTPUT:
The service ticket number is:  ST-16041-We3SligDEx0ImIBPTfPd-cas
Status of /host request:  200
  Number  Type      IP
--------  --------  -----------
       1  wireless  10.1.15.117
       2  wired     10.2.1.22
       3  wired     10.1.12.20
>>> 
'''
