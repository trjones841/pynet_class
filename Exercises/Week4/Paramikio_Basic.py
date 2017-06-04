
import paramiko
import time
#import getpass- use getpass.getpass('Password:') if using a true terminal

IPADDR = '192.168.0.121'
USER01 = 'tjones'
#PASSWD = getpass.getpass('Password:')
#PASSWD = raw_input('Password:')
PASSWD = 'Iam!g0ing'
PORT = 22
CMD = "show interfaces terse\n"

try:
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(IPADDR, username=USER01, password=PASSWD, look_for_keys=False, allow_agent=False,
                            port=PORT)
    remote_conn = remote_conn_pre.invoke_shell()

    #This works but exec_command closes the shell
    #stdin, stdout, stderr = remote_conn_pre.exec_command("show interface terse\n")
    #time.sleep(2)
    #print stdout.read()

    #Below is example for Cisco, but didn't work for Juniper
    output = remote_conn.send(CMD)
    output = remote_conn.recv(50000)
    remote_conn.settimeout(6.0)
    print remote_conn.gettimeout()

    #time.sleep(5)
    print "show interfaces terse: ", output

except paramiko.ssh_exception.SSHException:
    print "Exception Occurred...Something went strangely awry!"
    print paramiko.ssh_exception.SSHException
else:
    print "Completed"
