from abc import ABC,abstractmethod

class BaseAction(ABC):
    @abstractmethod
    def __init__(self):
        print ('bla')



