#!/usr/bin/env python

from abc import ABC, abstractmethod

class BasePackageManager(ABC):
    def __init__(self, pck_man_path):
        self.pck_man_path = pck_man_path