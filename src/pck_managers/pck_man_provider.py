#!/usr/bin/env python

from pck_managers import pacman_pck_man

def get_registered_pck_man():
    return {'pacman': pacman_pck_man.get_path(), 'dnf': '', 'yum': '', 'apt': '', 'apt-get': ''}