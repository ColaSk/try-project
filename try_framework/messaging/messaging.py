# -*- encoding: utf-8 -*-
'''
@File    :   messaging.py
@Time    :   2022/01/04 13:57:23
@Author  :   sk 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

from logging import getLogger
from abc import ABCMeta, abstractmethod

"""
Define message model
"""

_logger = getLogger(__name__)


# 消息
class MessageInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def read_header(self): pass

    @abstractmethod
    def write_header(self): pass

    @abstractmethod
    def read_body(self): pass

    @abstractmethod
    def write_body(self): pass


# json 消息实体
class JsonMessage(MessageInterface):

    def __init__(self, message: str):
        pass

    def read_header(self):
        pass

    def write_header(self):
        pass

    def read_body(self):
        pass

    def read_body(self):
        pass



