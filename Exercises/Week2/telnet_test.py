#!/usr/bin/python2.7
'''
Built & tested using Juniper SRX 220H - JUNOS 12.1X45-D15.5
'''

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    ip_addr = '192.168.0.121'
    username = 'tjones'
    password = 'A_aa0404'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.read_until("login:", TELNET_TIMEOUT)
    remote_conn.write(username + '\r\n')
    time.sleep(2)
    remote_conn.read_until("Password:", TELNET_TIMEOUT)
    remote_conn.write(password + '\r\n')
    time.sleep(2)
    remote_conn.write("show version | no-more" + '\n')
    time.sleep(3)
    output = remote_conn.read_very_eager()
    print "show version: ", output
    remote_conn.close()

if __name__ == "__main__":
    main()
