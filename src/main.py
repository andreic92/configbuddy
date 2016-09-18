#!/usr/bin/python

from lib import *

print(Globals.get_instance().__dict__)

cfg_parser = ConfigParser()
for action in cfg_parser.actions:
    action.execute()
