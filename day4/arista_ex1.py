#!/usr/bin/env python
"""
Use eapi to retrieve 'show ip route' from your arista switch.
From the returned data structure retrieve the prefixes, the output interfaces,
and the next hops (if available).

Print these routes and the associated information to stdout.
"""
from __future__ import print_function
from pprint import pprint
import pyeapi

def main():
    """
    Use eapi to retrieve 'show ip route' from your arista switch.
    From the returned data structure retrieve the prefixes, the output
    interfaces, and the next hops (if available).

    Print these routes and the associated information to stdout.
    """
    """
    connect_to() looks for info in "~/.eapi.conf" by default.
    [connection:pynet-sw4]
    username: eapi
    password: 17mendel
    host: 184.105.247.75
    transport: https
    """
    pynet_sw = pyeapi.connect_to("pynet-sw4")
    output = pynet_sw.enable("show ip route")

    # Strip off unneeded information
    output = output[0]
    output = output['result']['vrfs']['default']

    # Get the routes
    routes = output['routes']
    print("\n{:>15} {:>15} {:>15}".format("prefix", "interface", "next_hop"))
    filler = "-" * 15
    print("{:>15} {:>15} {:>15}".format(filler, filler, filler))
    for prefix, attr in routes.items():
        intf_nexthop = attr['vias'][0]
        interface = intf_nexthop.get('interface', 'N/A')
        next_hop = intf_nexthop.get('nexthopAddr', 'N/A')
        print("{:>15} {:>15} {:>15}".format(prefix, interface, next_hop))
    print()

if __name__ == "__main__":
    main()


'''
OUTPUT:

(py35_venv)[student12@ip-172-30-0-233 day4]$ ./arista_ex1.py

         prefix       interface        next_hop
--------------- --------------- ---------------
 10.220.88.0/24           Vlan1             N/A
      0.0.0.0/0           Vlan1     10.220.88.1

'''
