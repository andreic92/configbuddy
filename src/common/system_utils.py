#!/usr/bin/python

import os


def get_full_path(path):
    return os.path.abspath(path)

def execute_command(command):
    os.system(command)
