#!/usr/bin/python2.7

import pexpect
import sys
import time
import datetime
import re
from getpass import getpass

# pexpect.spawn.expect_exact = uses plain string matching instead of regex.
# expect_exact


def DateTime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st


def main():
    IPADDR = '192.168.0.121'
    USER = 'juniper'
    # PASSWD = getpass()
    PASSWD = 'juniper123'
    PORT = 22
    CMD = "show interfaces terse"

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(USER, IPADDR, PORT))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(PASSWD)
    ssh_conn.expect(USER + '@')
    try:
        ssh_conn.sendline(CMD + ' | no-more\n')
        ssh_conn.expect(USER + '@')
        print "Successful connection to :", IPADDR
        print "User :", USER
        print "\n", DateTime()
        print "\n", ssh_conn.before
        # print ssh_conn.after

    except pexpect.TIMEOUT:
        print "\nTimed Out"

    print "JUNOS Version :", reg_ex(ssh_conn)


def reg_ex(ssh_conn):
    pattern = re.compile(r'^JUNOS.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)

    return ssh_conn.after


if __name__ == "__main__":
    main()
