#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018
"""

import logging
import logging.handlers

 
class Logger(object):

    def __init__(
            self, name, path, 
            clevel = logging.INFO, Flevel = logging.DEBUG
    ):
        """ CRITICAL ERROR WARNING INFO DEBUG NOTSET """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(levelname)s][%(asctime)s]%(message)s', '%Y-%m-%d %H:%M:%S')
        """ 设置CMD日志 """
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        """ 设置文件日志 """
        # fh = logging.FileHandler(path)
        fh = logging.handlers.TimedRotatingFileHandler(path, when='D')
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def war(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)