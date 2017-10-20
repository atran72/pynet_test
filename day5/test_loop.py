#!/usr/bin/env python
from __future__ import print_function

ips = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4', '5.5.5.5']

for ip in ips:
    print(ip)

print('My Routers')
print('-' * 40)
routers = {
    'r1 = {'ip_addr = 1.1.1.1', 'dev_type = Juniper'}',
    'r2 = {'ip_addr = 2.2.2.2', 'dev_type = Cisco'}',
    'r3 = {'ip_addr = 3.3.3.3', 'dev_type = Arista'}'
    }

for rt in routers:
    print(router1 = rt.r1[0])
