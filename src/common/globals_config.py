#!/usr/bin/python

class Globals:
    def __init__(self, config):
        self.config = config
        self.__parse_config()

    def __parse_config(self):
        if self.config is None:
            raise Exception("Cannot parse invalid config!")
        print(self.config)

        for config_entry in self.config:
            for key, value in config_entry.items():
                setattr(self, key, value)

        print(self.__dict__)
