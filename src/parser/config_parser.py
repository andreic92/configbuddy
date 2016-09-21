#!/usr/bin/python

import sys
import os.path
import yaml
from action import *

class ConfigParser:

    """ On init read the config file and prepare the "self" values for "configs" and "packages"! """
    def __init__(self):
        self.config_path = os.path.dirname(self.__get_config_file())
        self.actions = self.__build_actions()

    """ Get the config file path from app arguments """
    def __get_config_file(self):
        arguments = sys.argv
        if len(arguments) <= 1:
            raise Exception("No config file specified!")
        config_file = arguments[1]
        if not os.path.isfile(config_file):
            raise Exception("Specified config \"%s\" does not exist!" % config_file)
        return config_file

    """ Read the config file """
    def __get_config(self):
        config_file_path = self.__get_config_file()
        with open(config_file_path, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                raise Exception("Couldn't load the config file \"%s\"" % config_file_path)

    """ Method for building the classes responsible for different actions (FileAction, PackageAction)"""
    def __build_actions(self):
        actions = []
        config = self.__get_config()
        for cfg in config:
            action_name = list(cfg.keys())[0]
            actions.append(globals()[action_name](cfg[action_name]))
        return actions
