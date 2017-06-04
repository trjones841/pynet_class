import paramiko,socket


# ssh function
def sshConnect(ip, username, password, command):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    try:
        client.connect(ip, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        #print stderr
        result_before = stdout.read()
        #print result_before
        result = result_before.splitlines()
        print "Success!! connection",
    except paramiko.AuthenticationException:
        print "Authentication problem"
        result = None
    except socket.error, e:
        print "Comunication problem "
        result = None
    client.close()
    return result

# main function
if __name__ == "__main__":
    ip = "10.100.0.100"
    username = "junos"
    password = "junos123"
    command = "show chassis alarm"
    result = sshConnect(ip, username, password, command)
    print result
