#!/usr/bin/python2.7

"""
tjones@SRX220-Py# show snmp 
v3 {
    usm {
        local-engine {
            user noauth {
                authentication-none;
            }
            user authnopriv {
                authentication-md5 {
                    authentication-key "$9$VEs2aiHmf5F-VQF69puX7N-24DjqTFnwYJDHqf5SrlvxNVwYZDilKWxN-2gTzF6tu1IceK836tO1RSywY24aUq.5T36s2JDHqQzSrlMxNgoJUDkg4n/9A1IYg4Zikz36/ApTQevLxdVTzF6p0hSrMWxyrZUiH5TEcSe8Xdbs2aZsYTzn6AtuO1Rre"; ## SECRET-DATA
                }
                privacy-none;
            }
            user authpriv {
                authentication-md5 {
                    authentication-key "$9$xr3-VYZGikqfLxmfQF/9vW8LVwaJD.fTNd2aGDkqIEhyM8xNdgaZhSlM8LVb.PfQ69pu1cSe5Q6Ap0IRNdVwYoDjq.5Q-V2aGDmPIEhrM8bs2oaUbwTzFnpudbwgZUP5Qzn/.mcyKMXx.PfQ/CBIErlMREgoZGq.O1IcevX7-VYg-d.PTQn69Ap0Ec"; ## SECRET-DATA
                }
                privacy-aes128 {
                    privacy-key "$9$/N40CtOhSrlvWB1yKMWx7.Pf569uO1EhrqmuO1IrloJZDjqmfT9tuPfcyKvLXqmPfFn9ApBRhtp0IEhrl8X7NdsYgoGjHY2TzF6AtvW8Lxdg4ZGjH4oDk.mTQevM8-Vg4ZGjHlKGDkqf5RhcrlMVwY2oJsYJDHqf5SrlKvL-VwoaUbwYoaJDjApu1Sr"; ## SECRET-DATA
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
                security-name noauth {
                    group v3test;
                }
                security-name authnopriv {
                    group v3test;
                }
                security-name authpriv {
                    group v3test;
                }
            }
        }
        access {
            group v3test {
                default-context-prefix {
                    security-model any {
                        security-level none {
                            read-view v3testview;
                            write-view v3testview;
                            notify-view v3testview;
                        }
                        security-level authentication {
                            read-view v3testview;
                            write-view v3testview;
                            notify-view v3testview;
                        }
                        security-level privacy {
                            read-view v3testview;
                            write-view v3testview;
                            notify-view v3testview;
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
            message-processing-model v2c;
            security-model usm;
            security-level authentication;
            security-name authnopriv;
        }
        notify-filter NOTIFY_FILTER;
    }
    notify-filter NOTIFY_FILTER {
        oid .1 include;
    }
    snmp-community v3test {
        security-name v3test;
    }
}
view v3testview {
    oid system include;
    oid .1 include;
}
community galileo {
    authorization read-write;
}


Reference - http://pysnmp.sourceforge.net/_downloads/usm-md5-des.py

$snmpget -v3 -l authPriv -u authpriv -A authentication1234 -X privacy1234 -a MD5 -x AES 192.168.0.121 SNMPv2-MIB::sysDescr.0

SNMPv2-MIB::sysDescr.0 = STRING: Juniper Networks, Inc. srx220h internet router, kernel JUNOS 12.1X45-D15.5 #0: 2013-09-19 07:42:15 UTC     
builder@svl-junos-pool92.juniper.net:/volume/build/junos/12.1/service/12.1X45-D15.5/obj-octeon/junos/bsd/kernels/JSRXNLE/kernel Build date: 2013-09


"""

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
