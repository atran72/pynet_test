#!/usr/bin/env python
from __future__ import print_function

my_list = ['Hey', 'Hallo', 'how', 'are', 'you']
my_list.append('whatever')
my_list.append('damn')
print(my_list.pop(0))

print("Length of list: {}".format(len(my_list)))
my_list.sort()
print(my_list)
