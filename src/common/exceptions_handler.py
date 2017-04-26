#!/usr/bin/python

from common import application_context
import logging

class ExceptionsHandler:

    def __init__(self):
        pass

    def handle(self, exception):
        if hasattr(application_context.ApplicationContext.get_instance().global_config, "exitOnError") and getattr(application_context.ApplicationContext.get_instance().global_config, "exitOnError") == "true":
            raise exception

        logging.info(exception)
