#!/usr/bin/env python

from __future__ import print_function

def my_func(x, y, z=20):
    data = {
        "x": "5",
        "y": "10",
        "z": "20",
    }

my_func(**data)


"""
Functions Ex2
--------------

Expand on functions exercise 1.

a. Create a list with three numbers
b. Use *args to call the function
c. Create a dictionary that has three keys of x, y, and z
d. Call the functions using **kwargs
"""
