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

def create_directory(path):
    os.makedirs(path)

def exists_file(path):
    return os.path.lexists(path)

def delete_file(path):
    os.remove(path)

def parse_dir(directory):
    if directory.endswith('/'):
        return directory
    return directory + '/'