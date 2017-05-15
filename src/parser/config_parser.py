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
        return self.__load_config(config_file_path)
        
    def __load_config(self, config_file_path):
        try:
            config = yaml.load(open(config_file_path))                                                                                                                                                                                  
            return self.__load_includes(config, os.path.dirname(config_file_path))
        except yaml.YAMLError as exc:
            raise Exception("Couldn't load the config file \"%s\"" % config_file_path)

    """ Method responsible for loading the imports array """
    def __load_includes(self, loaded_config, loaded_config_path):
        if "includes" not in loaded_config:
            return loaded_config

        for include in loaded_config.get("includes", []):
            included_config = self.__load_config("%s/%s" % (loaded_config_path ,include))
            for key, val in included_config.items():
                data = [] 
                if key in loaded_config:
                    data = loaded_config[key]
                data.extend(val)
                loaded_config[key] = data

        loaded_config.pop('includes')
        return loaded_config

    """ Method for building the classes responsible for different actions (FileAction, PackageAction)"""
    def __build_actions(self):
        actions = []
        config = self.__get_config()
        for key, val in config.items():
            if key == "Globals":
                logging.debug(key + " has the following config " + str(val))
                instance = Globals(val)
                ApplicationContext.get_instance().global_config = instance
                continue
            instances = self.__parse_current_action_content(key, val)
            actions.extend(instances) 
        quit()
        return actions

    def __parse_current_action_content(self, action_name, action_config_content):
        instances = []
        for individual_action_data in action_config_content:
            logging.debug(action_name + " has the following config " + str(individual_action_data))
            instance = globals()[action_name](individual_action_data)# like saying e.g. FileAction(<descriptive_object - required>)
            instances.append(instance)
        return instances

    def set_variables_on_context(self):
        appContext = ApplicationContext.get_instance()
        setattr(appContext.global_config, 'conf_dir', self.config_path)