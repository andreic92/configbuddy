#!/usr/bin/python

import yaml


class ConfigParser:
    def read_config(config_file):
        with open("test.yaml", 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)


