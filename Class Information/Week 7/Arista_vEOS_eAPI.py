#!/usr/bin/python2.7

'''
Code to use Arista's eAPI

Date: 14MAY2017

Author: tjones

'''

__author__ = 'tjones'

import jsonrpclib
from pprint import pprint

IPADDR = '192.168.0.40'
PORT = 80
USER = 'tjones'
PASSWD = 'A_aa0404'


def main(cmd):

    # TODO: Add SSL certificate to do https
    # SWITCH_URL = 'https://{}:{}@{}:{}/command-api'.format(USER, PASSWD, IPADDR, PORT)
    SWITCH_URL = 'http://{}:{}@{}:{}/command-api'.format(USER, PASSWD, IPADDR, PORT)
    print 'SWITCH_URL = ', SWITCH_URL
    remote_connect = jsonrpclib.Server(SWITCH_URL)
    response = remote_connect.runCmds(1, [cmd])
    print 'type: ', type(response)
    print '# of items in ', type(response), ': ', len(response)
    first_dictionary = response[0]
    print first_dictionary.keys()
    return response

def ipv4_neighbors(cmd):
    SWITCH_URL = 'http://{}:{}@{}:{}/command-api'.format(USER, PASSWD, IPADDR, PORT)
    print 'SWITCH_URL = ', SWITCH_URL
    remote_connect = jsonrpclib.Server(SWITCH_URL)
    response = remote_connect.runCmds(1, [cmd])
    dict = response[0]
    ipv4_neigh = dict['ipV4Neighbors']
    #print pprint(ipv4_neigh)
    print 'type: ', type(ipv4_neigh)
    print '# of items in ', type(ipv4_neigh), ': ', len(ipv4_neigh)
    for item in ipv4_neigh:
        pprint(item)
    return ipv4_neigh


def make_changes():
    commands = []
    commands.append('vlan 1000')
    commands.insert(0, 'configure terminal')
    commands.insert(0, {'cmd': 'enable', 'input': ''})
    commands.append('name Trust')
    print commands
    SWITCH_URL = 'http://{}:{}@{}:{}/command-api'.format(USER, PASSWD, IPADDR, PORT)
    remote_connect = jsonrpclib.Server(SWITCH_URL)
    response = remote_connect.runCmds(1, commands)
    pprint(response)
    # TODO: setup to make command list to take in new cmds for commands[2], commands[3] (for example)
    # will allow to iteratively add configuration w/o having to build new command strings
    return response

if __name__ == '__main__':
    #main('show arp')
    #ipv4_neighbors('show arp')
    make_changes()
