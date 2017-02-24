#!/usr/bin/python

def parse_destination_dir(directory):
    if directory.endswith('/'):
        return directory
    return directory + '/'
