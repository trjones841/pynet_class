#!/usr/bin/python2.7

from a10sdk.core.A10_import.import_periodic_ssl_cert import SslCert
from a10sdk.core.A10_import.A10WW_import import Import
from a10sdk.core.A10_file.file_ssl_cert_key import SslCertKey
from a10sdk.common.device_proxy import DeviceProxy
from getpass import getpass


IPADDR = '192.168.0.153'
PORT = '80'
USER = 'admin'
# PASSWD = getpass('Enter A10 Thunder password:')
PASSWD = 'a10'
CERT_FILE_HANDLE = '/tftpboot/SSL_TEST_CERT.crt'
CERT_KEY_FILE_HANDLE = '/tftpboot/SSL_TEST_CERT_KEY.key'
CERT_NAME = 'SSL_TEST_CERT2'
CERT_KEY_NAME = 'SSL_TEST_CERT_KEY'
CERTIFICATE_TYPE = 'pem'  # 'pem', 'der', 'pfx', 'p7b'
SVR_LOGIN = 'tjones'
# SVR_PASSWD = getpass('Enter server password:')
SVR_PASSWD = 'Iam!g0ing'

# dp = DeviceProxy(host=IPADDR, port=PORT, username=USER, password=PASSWD, use_https=False)


def import_cert():
    dp = DeviceProxy(host=IPADDR, port=PORT, username=USER, password=PASSWD, use_https=False)

    remote_file_url = 'scp://' + SVR_LOGIN + ':' + SVR_PASSWD + '@192.168.0.13:' + CERT_FILE_HANDLE
    file_ssl_cert_import = SslCert(certificate_type=CERTIFICATE_TYPE, period='315360000', DeviceProxy=dp)
    #file_ssl_cert_import = Import(ssl_cert=CERT_NAME, remote_file=remote_file_url, DeviceProxy=dp).file_upload(filename="SSL_TEST_CERT.crt", file_handle="/tftpboot", file_obj="ssl_cert")
    #print file_ssl_cert_import.remote_file
    #
    # filename = CERT_NAME, file_handle=CERT_FILE_HANDLE, file_obj='import'
    # print file_ssl_cert_import.file_upload(filename=CERT_NAME, file_handle=CERT_FILE_HANDLE, file_obj='txt')
    print "Output: ", file_ssl_cert_import.ERROR_MSG
    dp.logoff()

    return True


if __name__ == '__main__':
    import_cert()
