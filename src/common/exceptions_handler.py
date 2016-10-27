#!/usr/bin/python

from common.singleton import *

@Singleton
class ExceptionsHandler:

    def __init__(self):
        pass

    def handle(self, exception):
        if hasattr(self, "interrupt") and getattr(self, "interrupt") == "true":
            raise exception

        print(exception)