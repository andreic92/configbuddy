#!/usr/bin/python

from lib import BaseAction

class FileAction(BaseAction):

    def __init__(self, content):
        super(FileAction, self).__init__(content)
        #print("init file: %s" % content)

    def execute(self):
        print("file execute")
