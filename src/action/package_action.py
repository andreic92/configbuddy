#!/usr/bin/python

from action import BaseAction

class PackageAction(BaseAction):
    def __init__(self, content):
        super(PackageAction, self).__init__(content)

    def get_command(self):
        return ""

    def get_attrs_to_be_parsed(self):
        return []

    def parse_content(self, content):
        pass
