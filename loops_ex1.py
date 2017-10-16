#!/usr/bin/env python

from __future__ import print_function

my_list = list(range(1, 50))

for i in my_list:
    if i == 13:
        continue
    print(i)
    if i == 39:
        break
