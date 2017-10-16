#!/usr/bin/env python

ip = input("Enter the IP: ")
ip = ip.split(".")
print ("{:<12} {:<12} {:<12} {:<12}".format(*ip))
