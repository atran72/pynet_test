#!/usr/bin/env python

from __future__ import print_function

router = {
    'ip_addr': '1.1.1.1',
    'username': 'admin',
    'password': 'secret',
    'vendor': 'Juniper',
    'model': 'MX960',}

for k, v in router.items():
    print(k, v)

default_type = router.get('default_type', 'Cisco')
print("Default type is: {}")
