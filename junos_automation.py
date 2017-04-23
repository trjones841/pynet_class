#/usr/bin/python2.7

'''
# 
'''


from ncclient import manager
from ncclient.xml_ import *
import time
import datetime
import paramiko
import socket


# Returns current date time when called. Format == 2017-04-23 14:26:48
def DateTime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st


# JUNOS Automation: Example of "lock", "load_configuration", "validate", "commit", "discard_changes", "unlock" APIs:
# Uses the netconf interface
def connect(host, port, user, password, source):
    conn = manager.connect(host=host, port=port, username=user, password=password, timeout=10,
                           device_params={'name': 'junos'}, hostkey_verify=False)

    print 'locking configuration'
    lock = conn.lock()

    # build configuration element
    config = new_ele('system')
    sub_ele(config, 'host-name').text = 'SRX220-Py'
    sub_ele(config, 'domain-name').text = 'war-eagle.me'

    send_config = conn.load_configuration(config=config)
    print send_config.tostring

    check_config = conn.validate()
    print check_config.tostring

    compare_config = conn.compare_configuration()
    print compare_config.tostring

    print 'commit'
    # commit_config = conn.commit(confirmed=True, timeout='300')
    commit_config = conn.commit(timeout=None)
    print commit_config.tostring

    print 'sleeping for 5 sec...'
    time.sleep(5)

    discard_changes = conn.discard_changes()
    print discard_changes.tostring

    print 'unlocking configuration'
    unlock = conn.unlock()
    print unlock.tostring


# ssh function
def sshConnect(ip1, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    # client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip1, username=user, password=passwd, look_for_keys=False, allow_agent=False)
        stdin, stdout, stderr = client.exec_command(cmd)
        # print stderr
        result_before = stdout.read()
        # print result_before
        result = result_before
        print "Successful connection to :", ip1
        print "User :", user
        print "Date/Time :", DateTime(), "\n\n"
    except paramiko.AuthenticationException:
        print "Authentication problem"
        result = None
    except socket.error:
        print "Communication problem "
        result = None
    client.close()
    return result


# main function
if __name__ == "__main__":

    ip = "192.168.0.121"
    username = "juniper"
    password = "juniper123"
    command = "show interfaces terse"
    result = sshConnect(ip, username, password, command)
    print result

    # Calls the JUNOS automation ot change the hostname
    # connect('192.168.0.121', 830, 'juniper', 'juniper123', 'candidate')
