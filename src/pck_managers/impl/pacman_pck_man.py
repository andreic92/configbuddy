#!/usr/bin/env python

from pck_managers.base_pck_man import BasePackageManager
from common import application_context

class PacmanPackageManager(BasePackageManager):
    def __init__(self, pck_man_path):
        super(PacmanPackageManager, self).__init__(pck_man_path)
        self.install_command = "-Syu"
        self.remove_command = "-Ryu"
        self.repo_query_command = "-Si"
        self.local_query_command = "-Qi"

    def build_install_command(self, package_name):
        confirm_package = False
        if hasattr(application_context.ApplicationContext.get_instance().global_config, 'confirmEveryPackage') and getattr(application_context.ApplicationContext.get_instance().global_config, 'confirmEveryPackage') == 'true':
            confirm_package = True
        return "%s %s %s" % (self.pck_man_path, self.install_command, package_name)
        
    
def get_path():
    return __name__ + "." + PacmanPackageManager.__name__

    
