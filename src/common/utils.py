#!/usr/bin/python

def parse_dir(directory):
    if directory.endswith('/'):
        return directory
    return directory + '/'
