#!/usr/bin/python2.7

'''
This code is used to be able to used the pyeapi to connect to as Arista switch

.eapi.conf - file is located by default at: ~/
 [connection:py-veos01]
 USER: tjones
 PASSWD: A_aa0404
 IPADDR: 192.168.0.40
 PORT: 80
 PROTOCOL: http
'''

import pyeapi
import pprint as pp

veos01 = pyeapi.connect_to('veos01')

print veos01.enable('show version')

print dir(veos01)
# print help(veos01.get_config)
# print veos01.get_config()
#print(veos01.enable('show version'))
