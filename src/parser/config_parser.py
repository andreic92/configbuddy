#!/usr/bin/python

import sys
import os.path
import yaml
from common.globals_config import Globals
from action import *
from common.application_context import ApplicationContext
import logging

class ConfigParser:

    """ On init read the config file and prepare the "self" values for "configs" and "packages"! """
    def __init__(self):
        self.config_path = os.path.dirname(self.__get_config_file())
        self.actions = self.__build_actions()
        self.set_variables_on_context()

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
            if action_name == "Globals":
                logging.debug(action_name + " has the following config " + str(cfg[action_name]))
                instance = Globals(cfg[action_name])
                ApplicationContext.get_instance().global_config = instance
                continue
            instances = self.__parse_current_action_content(action_name, cfg[action_name])
            actions.extend(instances) # like saying e.g. FileAction(<descriptive_object - required>)
        return actions

    def __parse_current_action_content(self, action_name, action_config_content):
        instances = []
        for individual_action_data in action_config_content:
            logging.debug(action_name + " has the following config " + str(individual_action_data))
            instance = globals()[action_name](individual_action_data)
            instances.append(instance)
        return instances

    def set_variables_on_context(self):
        appContext = ApplicationContext.get_instance()
        setattr(appContext.constants, 'conf_dir', self.config_path)

        interrupt_on_exception = hasattr(appContext.global_config, 'exitOnError') and appContext.global_config.exitOnError is True
        setattr(appContext.exceptions_handler, "interrupt", interrupt_on_exception) 
