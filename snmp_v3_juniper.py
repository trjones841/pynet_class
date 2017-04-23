#!/usr/bin/python2.7

'''
tjones@SRX220-Py# show snmp    
v3 {
    usm {
        local-engine {
            user SNMP_USER {
                /* Password is: authenticate1234 */
                authentication-md5 {
                    authentication-key "$9$g2aJDiHmTQnq.5Fn6u07-dbs4HqmzF/TQSrKv7NqmP5369Ap0IEu0hrKMXxk.mf36AtOBEcikPQznCAuO1Ryl8LNsYo7NfTQ39CKMWLX-Y2aDjqg4Fn/CB17-dVwgGUHf5FmPF/AtOB7-dVgoJGDiqm4o69tpB1Vws2gJ.P5n6Af5hSreXxVwY4Uj"; ## SECRET-DATA
                }
                privacy-aes128 {
                    privacy-key "$9$A9JBp0IylKv8XREeWLX-dfTQzCtBIESyKP5BIEhKvZUDHkP5QFt0BTQreW87NP5TQ69tuORcy0O1hSyKvxNdVwg4aZjk.4oFn6Cu08Xx7-waJDjk.JZHmf5F3M8LxbsaJDjk.vWjHmPQzcyrKvLs24oZUg4UH.PQzlKvW87bs2ZGiY24ZGUHkuOBElK"; ## SECRET-DATA
                }
            }
        }
    }
    vacm {
        security-to-group {
            security-model usm {
                security-name SNMP_SECURITY_NAME {
                    group SNMP_GROUP_NAME;
                }
            }
        }
        access {
            group SNMP_GROUP_NAME {
                context-prefix CONTEXT-PREFIX {
                    security-model usm {
                        security-level authentication {
                            read-view SNMP_READ_VIEW;
                            write-view SNMP_WRITE_VIEW;
                            notify-view SNMP_NOTIFY_VIEW;
                        }
                    }
                }
            }
        }
    }
    target-address UBUNTU_DESKTOP01 {   
        address 192.168.0.182;
        timeout 600;
        target-parameters TARGET_PARATMETERS;
    }
    target-parameters TARGET_PARAMETERS {
        parameters {
            message-processing-model v3;
            security-model usm;
            security-level authentication;
            security-name SECURITY_NAME;
        }
        notify-filter NOTIFY_FILTER;
    }
    notify SNMP_NOTIFY {
        tag SNMP_NOTIFY_TAG;
    }
    notify-filter NOTIFY_FILTER {
        oid 1 include;
    }
    snmp-community COMMUNITY_INDEX {
        security-name SECURITY_NAME;
    }
}
view SNMP_NOTIFY_VIEW {
    oid .1 include;
}
view SNMP_READ_VIEW {
    oid 1.3.6.1.4;
}
view SNMP_WRITE_VIEW {
    oid 1.3.6.1.4.1;
}
community galileo {
    authorization read-write;
}

'''


from pysnmp.hlapi import *


def timeticks_2_time(timeticks):
    # Convert TimeTicks to days, hours:minutes.seconds
    d, h = divmod(timeticks, 8640000)
    h, m = divmod(h, 360000)
    m, s = divmod(m, 6000)
    s = s / 100

    #print "\n%d days, %02d:%02d.%02d" % (d, h, m, s)
    time_list = [d, h, m, s]
    return time_list

    '''
    # Alternative Method
    import datetime
    s = uptime/100
    print datetime.timedelta(seconds=s)
    '''


def __getsysUpTime():

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               UsmUserData('authpriv', 'authentication1234', 'privacy1234',
                           authProtocol=usmHMACMD5AuthProtocol,
                           privProtocol=usmAesCfb128Protocol),
               UdpTransportTarget(('192.168.0.121', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)))
    )
    print varBinds
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            number = timeticks_2_time(int(varBind[1]))
            print "\nsysUpTime (OID: %s): %2d days, %2d:%02d.%d" % (varBind[0], number.__getitem__(0), number.__getitem__(1),
                                                          number.__getitem__(2), number.__getitem__(3))


if __name__ == "__main__":
    __getsysUpTime()
