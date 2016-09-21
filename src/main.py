#!/usr/bin/python

from parser.config_parser import *

#print(Globals.get_instance().__dict__)
constants = Constants.get_instance()

cfg_parser = ConfigParser()
setattr(constants, 'conf_dir', cfg_parser.config_path)

actions_handler = ActionsHandler()
actions_handler.execute_actions(cfg_parser.actions)
