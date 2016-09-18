#!/usr/bin/python

from lib import BaseAction

class PackageAction(BaseAction):
    def __init__(self, content):
        super(PackageAction, self).__init__(content)

    def execute(self):
        print("package execute")
