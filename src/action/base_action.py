from abc import ABC, abstractmethod

from common import *
import os.path 

class BaseAction(ABC):

    @abstractmethod
    def __init__(self, content):
        self.content = content
        self.perform_before_parsing_content()
        self.parse_content(self.content)
        self.__replace_constants()

    """ Necessary method for getting a list of String objects that
        will be parsed against the system variables."""
    @abstractmethod
    def get_attrs_to_be_parsed(self):
        pass

    """ Necessary method for calling the required action that is 
        responsible for parsing the action content."""
    @abstractmethod
    def parse_content(self, content):
        pass

    """ Method needed to be implemented in order to force the
        implementations to return a valid command
    """
    @abstractmethod
    def get_command(self):
        pass

    """ Private method responsible for replacing the placeholders 
        with system variables.
    """
    def __replace_constants(self):
        for attr in self.get_attrs_to_be_parsed():
            for key, value in Constants.get_instance().get_available_variables().items():
                current_value = self.get_attribute(attr)
                self.set_attribute(attr, current_value.replace("$%s" % key, value))

    """ Method that allows actions to perform some actions before parsing the content
    """
    def perform_before_parsing_content(self):
        pass
    
    def get_attribute(self, key):
        if not hasattr(self, key):
            return None
        return getattr(self, key)

    def set_attribute(self, key, value):
        setattr(self, key, value)

    def get_full_path(self, path):
        return os.path.abspath(path)
