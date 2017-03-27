#!/usr/bin/python

from common.singleton import Singleton
from common.exceptions_handler import ExceptionsHandler
from common.constants import Constants
from common import system_utils
import logging

@Singleton
class ApplicationContext:

    def __init__(self):
        self.exceptions_handler = ExceptionsHandler()
        self.constants = Constants()
        self.global_config = None

    def execute_actions(self, actions):
        if actions is None:
            return
        for action in actions:
            command = action.get_command()
            logging.info(command)
            if not command:
                continue
            system_utils.execute_command(command)
