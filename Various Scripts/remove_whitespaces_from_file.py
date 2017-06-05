#!/bin/usr/python2.7


'''
This code will open a file (cfg-copy.txt) and will write all contents to a new file (cfg-2.txt) removing
all whitespace (blank lines) from the file
'''

fopen = open('/tmp/cfg-2.txt', 'w')

with open('/tmp/cfg-copy.txt', 'r') as file:
    for line in file:
        if not line.isspace():
            fopen.write(line)
