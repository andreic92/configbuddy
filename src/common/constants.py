#!/usr/bin/python

import getpass
import os
import pwd
import platform
import sys
import shutil
import importlib
from pck_managers.pck_man_provider import get_registered_pck_man

class Constants:
    user_variable = "USER"
    home_variable = "HOME"
    distro_variable = "DISTRO"
    package_manager_variable = "PCK_MANAGER"
    package_manager_class = "PCK_MANAGER_CLASS"

    def __init__(self):
        setattr(self, self.user_variable, getpass.getuser())
        setattr(self, self.home_variable, os.path.expanduser("~%s" % self.get_attr("USER")))
        setattr(self, self.distro_variable, platform.dist()[0])
        pck_man_path, pck_man_class = self.determine_package_manager()
        setattr(self, self.package_manager_variable, pck_man_path)
        setattr(self, self.package_manager_class, pck_man_class)

    def get_attr(self, attr_name):
        final_attr_name = attr_name.upper()
        if hasattr(self, final_attr_name):
            return getattr(self, final_attr_name)
        return None

    def determine_package_manager(self):
        if platform.system() != "Linux":
            raise Exception("Not supported system %s!" % platform.system())
        
        for pck_man, class_string in get_registered_pck_man().items():
            pck_man_path = shutil.which(pck_man)
            if pck_man_path is not None:
                return pck_man_path, self.str_to_class(class_string)
        raise Exception("No package manager found!")

    def get_available_variables(self):
        return self.__dict__

    def str_to_class(self, fully_qualified_name):
        module_name = fully_qualified_name.rsplit('.', 1)[0]
        class_name = fully_qualified_name.rsplit('.', 1)[-1]
        try:
            module_ = importlib.import_module(module_name)
            try:
                class_ = getattr(module_, class_name)
            except AttributeError:
                logging.error('Class does not exist')
        except ImportError:
            logging.error('Module does not exist')

        return class_ or None
