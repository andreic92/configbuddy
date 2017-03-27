#!/usr/bin/python

from parser.config_parser import ConfigParser
from common.application_context import ApplicationContext
import logging

logging.basicConfig(level=1)
cfg_parser = ConfigParser()

ApplicationContext.get_instance().execute_actions(cfg_parser.actions)


