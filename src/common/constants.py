#!/usr/bin/python

import getpass
import os
import pwd
import platform

class Constants:
    user_variable = "USER"
    home_variable = "HOME"
    distro_variable = "DISTRO"
    package_manager_variable = "PCK_MANAGER"

    def __init__(self):
        setattr(self, self.user_variable, getpass.getuser())
        setattr(self, self.home_variable, os.path.expanduser("~%s" % self.get_attr("USER")))
        setattr(self, self.distro_variable, platform.dist()[0])
        setattr(self, self.package_manager_variable, self.determine_package_manager(self.get_attr("DISTRO")))

    def get_attr(self, attr_name):
        final_attr_name = attr_name.upper()
        if hasattr(self, final_attr_name):
            return getattr(self, final_attr_name);
        return None

    def determine_package_manager(self, distro_name):
        if platform.system() != "Linux":
            raise Exception("Not supported system %s!" % platform.system())

        ## TODO
        return "test"

    def get_available_variables(self):
        return self.__dict__
