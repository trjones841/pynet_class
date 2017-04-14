from snmp_helper import snmp_get_oid, snmp_extract


def snmp_print():
    COMMUNITY_STRING = 'galileo'
    SNMP_PORT = 161
    #IP = '54.183.67.229'
    IP = '192.168.0.121'

    a_device = (IP, COMMUNITY_STRING, SNMP_PORT)

    for i in range(0, 10, 1):
        OID = "1.3.6.1.2.1.1."+str(i)+".0"
        snmp_data = snmp_get_oid(a_device, oid=OID)
        output = snmp_extract(snmp_data)
        print OID
        print "i:", i, "    output:", output

if __name__ == "__main__":
    snmp_print()
