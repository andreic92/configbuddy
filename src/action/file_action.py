#!/usr/bin/python

from action import *
from common import system_utils
from common import utils
from common import constants
from common import exceptions_handler

class FileAction(BaseAction):

    def __init__(self, content):
        super(FileAction, self).__init__(content)

    def get_attrs_to_be_parsed(self):
        return ['destination']

    def get_command(self):
        command = self.get_attribute('command')
        file_name = self.get_attribute('file_name')
        source_relative = self.get_attribute('source')
        file_path = system_utils.get_full_path(constants.Constants.get_instance().conf_dir + "/" + source_relative + "/" + file_name)
        destination = utils.parse_dir(self.get_attribute('destination'))
        final_destination = destination + self.__get_file_name() 
        if system_utils.exists_file(final_destination):
            system_utils.delete_file(final_destination)
        """ if parse_child attribute is present create commands for the each file contained in the current director """
        if self.get_attribute('parse_child'):
            return self.__generate_child_commands(command, file_path, destination)

        self.__create_destination(destination)
        return "%s %s %s" % (command, file_path, final_destination)

    def __generate_child_commands(self, command, parent_path, destination):
        try:
            print(system_utils.list_files(parent_path))
        except NotADirectoryError as directory_exception:
            exceptions_handler.ExceptionsHandler.get_instance().handle(directory_exception)

    def parse_content(self, content):
        for file_name, properties in content.items():
            setattr(self, 'file_name', file_name)
            for prop_key, prop_val in properties[0].items():
                setattr(self, prop_key, prop_val)
                    

    def __get_file_name(self):
        file_name = self.file_name
        if self.hidden is True:
            file_name = '.' + file_name
        return file_name

    def __create_destination(self, destination):
        if not system_utils.exists_file(destination):
            system_utils.create_directory(destination)
