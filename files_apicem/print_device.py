#Print devices from sandboxapicem

import requests
import json
from tabulate import *
from my_apic_em_functions import *


api_url = "https://SandBoxAPICEM.cisco.com/api/v1/network-device"
ticket = get_ticket()
headers = {
    "content-type": "application/json",
    "X-Auth-Token": ticket
}
resp = requests.get(api_url, headers=headers, verify=False)
print("Status of /device request: ", resp.status_code)
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)
response_json = resp.json()
device_list = []
i = 0
for item in response_json["response"]:
    i += 1
    device = [
            i, 
            item["type"], 
            item["managementIpAddress"] 
           ]
    device_list.append( device )

table_header = [
                "Number",
                "Type",
                "IP"
               ]
print( tabulate(device_list, table_header) )

'''
OUTPUT:
The service ticket number is:  ST-16122-QgfGZucVR9kSSpQmgyGY-cas
Status of /device request:  200
  Number  Type                                            IP
--------  ----------------------------------------------  -------------
       1  Cisco 3500I Unified Access Point                10.1.14.3
       2  Cisco Catalyst 29xx Stack-able Ethernet Switch  10.2.1.17
       3  Cisco 2911 Integrated Services Router G2        10.2.2.1
       4  Cisco 2911 Integrated Services Router G2        10.2.2.2
       5  Cisco 2911 Integrated Services Router G2        218.1.100.100
       6  Cisco Catalyst 3850-48U-E Switch                10.1.12.1
       7  Cisco Catalyst 6503 Switch                      10.1.7.1
       8  Cisco Catalyst 6503 Switch                      10.1.10.1
       9  Cisco Catalyst 4507R plus E Switch              10.255.1.5
      10  Cisco Catalyst 4507R plus E Switch              10.1.11.1
      11  Cisco 4451 Series Integrated Services Router    10.1.2.1
      12  Cisco 4451 Series Integrated Services Router    10.1.4.2
      13  Cisco 5508 Wireless LAN Controller              10.1.14.2
>>> 
'''
