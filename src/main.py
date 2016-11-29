#!/usr/bin/python

from parser.config_parser import *

constants = Constants.get_instance()
exceptions_handler = ExceptionsHandler.get_instance()

cfg_parser = ConfigParser()
cfg_parser.set_variables_on(constants, exceptions_handler)

actions_handler = ActionsHandler()
actions_handler = ActionsHandler()
actions_handler.execute_actions(cfg_parser.actions)
