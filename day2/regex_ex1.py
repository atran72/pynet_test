#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals
import re

with open('show_int_fa4.txt') as f:
    output = f.read()

patterns = {
    "Input": r"(\d+) packets input, (\d+) bytes",
    "Output": r"(\d+) packets output, (\d+) bytes"
}

for label, pattern in patterns.items():
    match = re.search(pattern, output)
    if match:
        print("\n{}: ".format(label))
        print("Packets: {}".format(match.group(1)))
        print("Bytes: {}\n".format(match.group(2)))




"""
RegEx Ex1
----------

1. Use the 'show interface fa4' output (in the file 'show_int_fa4.txt').

2. Use regular expressions extract the following:
    a. packets input/output
    b. bytes input/output
"""
