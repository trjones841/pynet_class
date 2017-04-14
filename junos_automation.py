#/usr/bin/python2.7

'''
# Example of "lock", "load_configuration", "validate", "commit", "discard_changes", "unlock" APIs:
'''

from ncclient import manager
from ncclient.xml_ import *

import time

def connect(host, port, user, password, source):
    conn = manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            device_params = {'name':'junos'},
            hostkey_verify=False)

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
    #commit_config = conn.commit(confirmed=True, timeout='300')
    commit_config = conn.commit(timeout=None)
    print commit_config.tostring

    print 'sleeping for 5 sec...'
    time.sleep(5)

    discard_changes = conn.discard_changes()
    print discard_changes.tostring

    print 'unlocking configuration'
    unlock = conn.unlock()
    print unlock.tostring

if __name__ == '__main__':
    connect('192.168.0.121', 830, 'tjones', 'Iam!g0ing', 'candidate')
