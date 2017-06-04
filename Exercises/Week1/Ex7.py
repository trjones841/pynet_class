#!/usr/bin/python2.7

'''
Week1
Ex7 - Read in lists from Ex6 and ensure pretty print the struct
'''


def main():

    yamlfile = 'data.yml'
    jsonfile = 'data.json'

    yfile = open(yamlfile, "r").read().splitlines()
    for line in yfile:
        print line

    jfile = open(jsonfile, "r").read().splitlines()
    for line in jfile:
        print line

if __name__ == '__main__':
    main()
