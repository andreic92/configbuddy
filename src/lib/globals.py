#!/usr/bin/python
import sys
import os.path
import yaml

def get_config_file():
    arguments = sys.argv
    if len(arguments) <= 1:
        raise Exception("No config file specified!")
    config_file = arguments[1]
    if not os.path.isfile(config_file):
        raise Exception("Specified config \"%s\" does not exist!" % config_file)

    return config_file

def get_config():
    config_file_path = get_config_file()
    with open(config_file_path, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            raise Exception("Couldn't load the config file \"%s\"" % config_file_path)



