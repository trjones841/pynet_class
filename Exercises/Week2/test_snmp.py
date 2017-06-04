#!/usr/bin/python2.7

import pysnmp

def snmpwalk1():

    print "pysnmp.verision: ", pysnmp.version
    print "pysnmp.__name__: ", pysnmp.__name__
    return

if __name__ == "__main__":
    snmpwalk1()
