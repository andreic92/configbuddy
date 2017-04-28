#!/usr/bin/env python

from pck_managers.impl import *
from collections import OrderedDict


def get_registered_pck_man():
    registered_pck_man = OrderedDict()
    registered_pck_man['pacman'] = pacman_pck_man.get_path()
    registered_pck_man['dnf'] = ''
    registered_pck_man['yum'] = ''
    registered_pck_man['apt'] = apt_pck_man.get_path()
    registered_pck_man['apt-get'] = apt_pck_man.get_path()
    return registered_pck_man