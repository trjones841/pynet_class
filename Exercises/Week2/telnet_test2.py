#!/etc/python2.7
'''
Built & tested using Juniper SRX 220H - JUNOS 12.1X45-D15.5
'''


import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\r\n')
    time.sleep(1)
    return remote_conn.read_very_eager()


def login(remote_conn, username, password):
    remote_conn.read_until("login:", TELNET_TIMEOUT)
    remote_conn.write(username + '\r\n')
    time.sleep(1)
    remote_conn.read_until("Password:", TELNET_TIMEOUT)
    remote_conn.write(password + '\r\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    return output


def telnet_connection(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed out")
    except socket.error:
        print sy
        sys.exit("You received an error")


def main():
    ip_addr = '192.168.0.121'
    username = 'tjones'
    password = 'A_aa0404'

    remote_conn = telnet_connection(ip_addr)
    login(remote_conn, username, password)
    output = send_command(remote_conn, "show config interfaces | no-more" + '\n')
    time.sleep(2)
    print output
    remote_conn.close()


if __name__ == "__main__":
    main()
