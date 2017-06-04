#!/usr/bin/python2.7

from netmiko import ConnectHandler
from getpass import getpass

#PASSWD = getpass()
PASSWD = 'juniper123'

juniper_srx220 = {
    'device_type': 'juniper',
    'ip': '192.168.0.121',
    'username': 'juniper',
    'password': PASSWD,
}

srx220_pynet = ConnectHandler(**juniper_srx220)
# dir(srx220_pynet)  # Check available classes
print srx220_pynet.send_command('show arp')

#config_commands = ['set system host-name SRX220_pynet']
#srx220_pynet.send_config_set(config_commands)
#srx220_pynet.commit('commit and-quit')
print srx220_pynet.send_command('exit\n')

