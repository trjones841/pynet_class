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

