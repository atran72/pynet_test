#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals
import re
from pprint import pprint

with open('show_mac_multicast.txt') as f:
    output = f.read()

# print(output)
entry = re.split(r'^------.*---------------$', output, flags=re.M)[1]
entry = entry.split()
pattern = r'^(\d+)





"""
RegEx Ex2
----------

1. Use the partial show mac table information contained in the file "show_mac_multicast.txt"

2. Use regular expressions to create the following data structure:

    {'ffff.ffff.ffff':
        {
            'vlan': 11,
            'type': 'system'
            'ports': ['Gi2/4', 'Gi2/5', ... 'Gi3/15']
        }
    }
"""
