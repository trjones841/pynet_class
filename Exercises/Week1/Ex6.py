#!/usr/bin/python2.7

'''
Week1
Ex6 - Create a list. One element of list should be a dictionary with min 2 keys.
Write out list using both Yaml and JSON formats.

'''
import yaml
import json

def main():

    yamlfile = 'data.yml'
    jsonfile = 'data.json'

    dict_one = {
        'one' : 'uno',
        'two' : 'dos'
    }
    dict_two = {
        'three': 'tres',
        'four' : 'cuatro',
        'five' : 'cinco'
    }
    NEW_LIST = ['one', 'two', 'three', 'four', dict_one, 'five', dict_two]

    with open(yamlfile, "w") as yf:
        #print yaml.dump(NEW_LIST, default_flow_style=False)
        yf.write(yaml.dump(NEW_LIST, default_flow_style=False))

    with open(jsonfile, "w") as jf:
        #print json.dumps(NEW_LIST, sort_keys=True, indent=4, separators=(',', ':'))
        jf.write(json.dumps(NEW_LIST, sort_keys=True, indent=4, separators=(',', ':')))

    return True

if __name__ == '__main__':
    main()
