#!/usr/bin/python3

from parser.config_parser import ConfigParser
from common.application_context import ApplicationContext
import logging

logging.basicConfig(level=1)
cfg_parser = ConfigParser()
ApplicationContext.get_instance().execute_actions(cfg_parser.actions)

# testing
#ApplicationContext.get_instance()#.execute_actions(cfg_parser.actions)
#b = ApplicationContext.get_instance().constants.PCK_MANAGER_CLASS(ApplicationContext.get_instance().constants.PCK_MANAGER).build_install_command('parcellite')
#print(b)