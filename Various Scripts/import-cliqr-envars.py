#!/usr/bin/python2.7
import os
import sys

def set_cliqr_envars():
    fname = r'/tftpboot/cliqr_envs.txt'
    with open(fname, 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    env_variables = []
    for item in content:
        env_variables.append(item.split("="))
    for env, value in env_variables:
        print 'env: ', env, '     value: ', value
        os.environ[env]= value
    return True


if __name__ == '__main__':

    DEBUG_OFFLINE = 'True'

    print "DEBUG_OFFLINE: ", DEBUG_OFFLINE

    if DEBUG_OFFLINE == 'True':
        set_cliqr_envars()
        sys.argv[0] = 'update'   #start, update, stop
        cmd = sys.argv[0]
        print 'Debugging mode using file of static variables'
    elif True:
        #cmd = sys.argv[1]
        print
