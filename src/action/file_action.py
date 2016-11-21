#!/usr/bin/python

from action import *
from common import *

class FileAction(BaseAction):

    def __init__(self, content):
        super(FileAction, self).__init__(content)

    def get_attrs_to_be_parsed(self):
        return ['destination']

    def get_command(self):
        command = self.get_attribute('command')
        file_path = get_full_path(Constants.get_instance().conf_dir + "/" + self.get_attribute('file_name'))
        destination = self.get_attribute('destination')
        """ if parse_child attribute is present create commands for the each file contained in the current director """
        if self.get_attribute('parse_child'):
            return self.__generate_child_commands(command, file_path, destination)

        return "%s %s %s" % (command ,file_name, destination)

    def __generate_child_commands(self, command, parent_path, destination):
        try:
            print(list_files(parent_path))
        except NotADirectoryError as directory_exception:
            ExceptionsHandler.get_instance().handle(directory_exception)

    def parse_content(self, content):
        for value in content:
            for file_name, properties in value.items():
                setattr(self, 'file_name', file_name)
                for prop_key, prop_val in properties[0].items():
                    setattr(self, prop_key, prop_val)
