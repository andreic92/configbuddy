#!/usr/bin/python

from parser.config_parser import ConfigParser
from common.constants import Constants
from common.exceptions_handler import ExceptionsHandler
from common.actions_handler import ActionsHandler

constants = Constants.get_instance()
exceptions_handler = ExceptionsHandler.get_instance()

cfg_parser = ConfigParser()
cfg_parser.set_variables_on(constants, exceptions_handler)

actions_handler = ActionsHandler()
actions_handler.execute_actions(cfg_parser.actions)
