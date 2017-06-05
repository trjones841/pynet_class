# !/usr/bin/env python
import os
import pprint

print os.environ['HOME']
print os.environ['LOGNAME']
print os.environ['USER']
print os.environ['PATH']
print os.error
print os.name
print os.getcwd()
print os.getcwdu()
# os.chdir('/tmp/new/path')
# os.chroot(path)
# os.chmod(path, mode)  # mode = stat.S_ITREAD, stat.S_IWRITE, stat.S_IEXEC, , stat.S_IWUSR
# os.chown(path, uid, gid)
# os.link(source, link_name)
for item in (os.listdir('/media/tjones/SSD21/Networking/Python')):
    print item
print os.lstat('/tmp')

# os.makedir(path['mode])
# os.mkdir('/media/tjones/SSD21/Networking/Python/A10', 0777)
# os.rename(src,dst)
# os.rmdir('/media/tjones/SSD21/Networking/Python/A10')
# os.symlink(source, link_name)

# os.abort()
# os.kill=(pid,sig)
# os.killpg(pgid,sig)
# os.nice(increment)
# os.plock(op)
# os.system(command)
print os.system('date')
print os.times()
# os.wait()
print os.getloadavg()
print os.sysconf('SC_NPROCESSORS_ONLN')
print os.sysconf('SC_OPEN_MAX')
print os.curdir
print os.urandom(3)


