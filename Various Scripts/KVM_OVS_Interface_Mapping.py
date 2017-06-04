#!/usr/bin/python2.7

"""


Add - Make script add VM interfaces to the correct bridge

    #ifconfig | grep ma:ca:dd:re:ss:00 (only match last 2 bytes)
    #sudo ovs-vsctl del-port br5 vnet
    #sudo ovs-vsctl add-port br5 vnet tag=30
    #sudo ifconfig vnet up


Add - auto mount STORAGEIV 


"""
import paramiko
import time
#import getpass- use getpass.getpass('Password:') if using a true terminal

IPADDR = '192.168.0.12'
USER01 = 'tjones'
#PASSWD = getpass.getpass('Password:')
#PASSWD = raw_input('Password:') # not clear txt
PASSWD = 'Iam!g0ing'
PORT = 22

#Devices = Interface:mac_address
vThunder01 =       [['br3', '', 've3', '52:54:00:a6:d3:36'],
                    ['br5', '30', 've30', '52:54:00:99:b7:f1'],
                    ['br100', '', 've100', '52:54:00:7b:5d:e6']]
vThunder02 =       [['br3', '', 've3', '52:54:00:22:fe:62'],
                    ['br5', '30', 've30', '52:54:00:3c:86:4c'],
                    ['br100', '', 've100', '52:54:00:ab:ef:35']]
vThunder03 =       [['br6', '', 've6', '52:54:00:d2:c7:dc'],
                    ['br5', '31', 've31', '52:54:00:dd:6a:f4'],
                    ['br7', '', 've7', '52:54:00:a9:f9:59']]
vThunder04 =       [['br6', '', 've6', '52:54:00:8f:53:60'],
                    ['br5', '31', 've31', '52:54:00:ec:ac:70'],
                    ['br7', '', 've7', '52:54:00:2f:2d:ed']]
MINT01 =           [['br0', '', 'eth0', '52:54:00:e4:c0:44'],
                    ['br2', '', 'eth1', '52:54:00:18:2f:cd'],
                    ['br5', '30', 'eth2', '52:54:00:13:02:42'],
                    ['br5', '31', 'eth3', '52:54:00:e4:85:9c'],
                    ['br15', '', 'eth4', '52:54:00:ab:65:76']]
MINT02 =           [['br0', '', 'eth0', '52:54:00:5a:ab:f9'],
                    ['br2', '', 'eth1', '52:54:00:e0:69:c6'],
                    ['br5', '30', 'eth2', '52:54:00:a0:4d:40'],
                    ['br11', '', 'eth3', '52:54:00:63:71:63'],
                    ['br15', '', 'eth4', '52:54:00:ad:d1:4e']]
MINT03 =           [['br0', '', 'eth0', '52:54:00:e9:8a:47'],
                    ['br3', '', 'eth1', '52:54:00:99:81:48'],
                    ['br5', '31', 'eth2', '52:54:00:1d:ce:0c'],
                    ['br9', '', 'eth3', '52:54:00:e0:1d:b2'],
                    ['ext-br0', '', 'eth4', '52:54:00:76:16:1a']]
MINT04 =           [['br0', '', 'eth0', '52:54:00:20:79:0e'],
                    ['br3', '', 'eth1', '52:54:00:8d:1c:72'],
                    ['br5', '31', 'eth2', '52:54:00:9d:43:ad'],
                    ['br9', '', 'eth3', '52:54:00:4e:d9:fb'],
                    ['ext-br0', '', 'eth4', '52:54:00:b5:81:72']]
UBUNTU_DESKTOP01 = [['br0', '', 'eth0', '52:54:00:50:02:db'],
                    ['br3', '', 'eth1', '52:54:00:63:16:b1'],
                    ['br1', '31', 'eth2', '52:54:00:47:ad:41'],
                    ['br10', '', 'eth3', '52:54:00:5f:6a:bd'],
                    ['br40', '', 'eth4', '52:54:00:ce:db:a5']]
VyOS_01 =          [['br0', '', 'eth0', '52:54:00:81:ca:49'],
                    ['br40', '', 'eth1', '52:54:00:85:3d:67'],
                    ['br7', '', 'eth2', '52:54:00:ae:20:db'],
                    ['br8', '', 'eth3', '52:54:00:94:04:83'],
                    ['br6', '', 'eth4', '52:54:00:63:02:31'],
                    ['br8', '', 'eth5', '52:54:00:ac:21:0c'],
                    ['br11', '', 'eth6', '52:54:00:c1:7a:ce']]
VyOS_02 =          [['br51', '', 'eth0', '52:54:00:80:34:aa'],
                    ['br40', '', 'eth5', '52:54:00:41:76:ef'],
                    ['br5', '30', 'eth6', '52:54:00:56:db:a1'],
                    ['br5', '31', 'eth7', '52:54:00:14:d3:3f'],
                    ['br0', '', 'eth8', '52:54:00:a3:c0:fc'],
                    ['br7', '', 'eth9', '52:54:00:53:b0:c9']]
vMX02 =            [['br0', '', 'em0', '52:54:00:23:c5:80'],
                    ['br1', '', 'em1', '52:54:00:7e:35:e4'],
                    ['ext-br0', '', 'em2', '52:54:00:2f:bd:79'],
                    ['br12', '', 'em3', '52:54:00:5a:20:c7'],
                    ['br3', '', 'em4', '52:54:00:13:4c:f4'],
                    ['br40', '', 'em5', '52:54:00:9b:5a:1f'],
                    ['br100', '', 'em6', '52:54:00:95:0c:45'],
                    ['br5', '30', 'em7', '52:54:00:f7:59:2f']]
vMX03 =            [['br0', '', 'em0', '52:54:00:e3:fa:38'],
                    ['br151', '', 'em1', '52:54:00:67:93:84'],
                    ['br101', '', 'em2', '52:54:00:67:93:84'],
                    ['br1', '', 'em3', '52:54:00:06:53:2a'],
                    ['br2', '', 'em4', '52:54:00:06:53:2a'],
                    ['br8', '', 'em5', '52:54:00:06:53:2a'],
                    ['br13', '', 'em6', '52:54:00:f7:4b:9b'],
                    ['br11', '', 'em7', '52:54:00:29:98:e1']]
WIN10 =            [['br0', '', 'TRUST', '52:54:00:83:be:91'],
                    ['br1', '', 'SSLi', '52:54:00:e4:15:e6'],
                    ['br5', '30', 'VLAN30', '52:54:00:da:21:91']]
BADSTORE =         [['br5', '30', 'VLAN30', '52:54:00:5a:3c:e1']]
WEB-CASINO =         [['br5', '30', 'VLAN30', '52:54:00:da:21:91']]

List_Of_Devices = (vThunder01, vThunder02, vThunder03, vThunder04, VyOS_01, VyOS_02, MINT01, MINT02, MINT03, MINT04,
                   UBUNTU_DESKTOP01)


def get_bridge_mac_list(response):
    LIST_BR_T0_MAC = []
    for row in response.split('\n'):
        if 'br' in row:
            output = row.split(" ")
            bridge = output[0]
            find_mac = row.split('HWaddr')
            mac = find_mac[1]
            LIST_BR_T0_MAC.append([bridge, mac])
    #for item in LIST_BR_T0_MAC:
    #    print item
    return LIST_BR_T0_MAC


def get_vnet_list(ifconfig_output):
    # Returns a list of mac addresses corresponding to the current list of vnet interfaces on the linux box.
    LIST_VNET_T0_MAC = []
    for row in ifconfig_output.split('\n'):
        if 'vnet' in row:
            output = row.split(" ")
            bridge = output[0]
            find_mac = row.split('HWaddr')
            mac = find_mac[1]
            LIST_VNET_T0_MAC.append([bridge, mac])
    # for item in LIST_VNET_T0_MAC:
    #   print item
    return LIST_VNET_T0_MAC


def parse_mac(mac_add):
    pairs = mac_add.split(':')
    #print pairs
    concate = pairs[4] + ':' + pairs[5]
    return concate


def update_mappings(list_of_vnets):
    count = 0
    for item in List_Of_Devices:
        for i in item:
            mac_check = parse_mac(i[3])
            for vnet, mac in list_of_vnets:
                if str(parse_mac(mac)).strip(" ") == mac_check:
                    # print "\nMatch: parse_mac()", parse_mac(mac), "==   mac_check: ", mac_check
                    print "sudo ovs-vsctl del-port " + i[0] + " " + vnet
                    if i[1] == "":
                        print "sudo ovs-vsctl add-port " + i[0] + " " + vnet
                    else:
                        print "sudo ovs-vsctl add-port " + i[0] + " " + vnet + " tag=" + i[1]
                    print "sudo ifconfig " + vnet + " up\n"
    return True

def run_cmds(CMD):
    try:
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(IPADDR, username=USER01, password=PASSWD, look_for_keys=False, allow_agent=False,
                                port=PORT)
        remote_conn = remote_conn_pre.invoke_shell()
        time.sleep(2)

        stdin, stdout, stderr = remote_conn_pre.exec_command(CMD)
        remote_conn.settimeout(6.0)
        time.sleep(1)
        response = stdout.read()
        # BRIDGE_MAC_LIST = get_bridge_mac_list(response)
        vnet_list = get_vnet_list(response)
        update_mappings(vnet_list)

    except paramiko.ssh_exception.SSHException:
        print "Exception Occurred...Something went strangely awry!"
        print paramiko.ssh_exception.SSHException
    else:
        print "Completed"

    return True


if __name__ == '__main__':
    print "\nRunning\n"
    run_cmds(CMD="ifconfig\n")

