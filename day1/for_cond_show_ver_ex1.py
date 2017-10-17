#!/usr/bin/env python

from __future__ import print_function

# Read a show version output from a router (in a file)
with open('show_version.txt') as f:
    show_ver = f.read().splitlines()

for line in show_ver:
    if 'Processor board ID' in line:
        serial_number = line.split()
        print(serial_number)


"""
(py35_venv)[student12@ip-172-30-0-233 day1]$ ./for_cond_show_ver_ex1.py
['Processor', 'board', 'ID', 'FTX1512038X']
"""
