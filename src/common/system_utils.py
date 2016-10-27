#!/usr/bin/python

import os


def get_full_path(path):
    return os.path.abspath(path)

def execute_command(command):
    if isinstance(command, list):
        for comm in command:
            os.system(command)
        return

    os.system(command)

def list_files(path):
    return os.listdir(path)
