#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from getpass import getpass
from pprint import pprint

juniper_srx = {
    "host": "srx1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}

print()
for device in [juniper_srx]:
    a_device = Device(**device)
    a_device.open()
    ss = StartShell(a_device)
    ss.open()
    ss.run('cli -c "request support information | save /var/tmp/information.txt"')
    version = ss.run('cli -c "show version"')
    print(version)
    ss.close()
    a_device.close()

print()


'''
from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell

dev = Device(host='router1.example.net')
dev.open()

ss = StartShell(dev)
ss.open()
ss.run('cli -c "request support information | save /var/tmp/information.txt"')
version = ss.run('cli -c "show version"')
print (version)
ss.close()

dev.close()
'''
