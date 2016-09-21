#!/usr/bin/python

from common.system_utils import *

class ActionsHandler:
    def __init__(self):
        pass

    def execute_actions(self, actions):
        if actions is None:
            return
        for action in actions:
            command = action.get_command()
            if not command:
                continue
            execute_command(command)
