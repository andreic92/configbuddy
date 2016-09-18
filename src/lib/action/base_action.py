from abc import ABC, abstractmethod

from lib import Globals

class BaseAction(ABC):
    @abstractmethod
    def __init__(self, content):
        self.replace_constants(content)

    def replace_constants(self, content):
        if content is None:
            raise Exception("Content cannot be null!")

        Globals.get_instance().get_available_variables()
