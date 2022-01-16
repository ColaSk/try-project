# -*- encoding: utf-8 -*-
'''
@File    :   spawning.py
@Time    :   2022/01/04 18:05:38
@Author  :   sk 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

"""Execution node spawn
"""

class SpawningProxy(object):

    def __init__(self, items):
        self._items = items

    def __getattr__(self, name):
        def spawning_method(*args, **kwargs):
            items = self._items
            if items:
                def call(item):
                    return getattr(item, name)(*args, **kwargs)
                return [call(i) for i in items]

        return spawning_method

class SpawningSet(set):
    """ A set with an ``.all`` property that will spawn a method call on each
    item in the set into its own (parallel) greenthread.
    """
    @property
    def all(self):
        return SpawningProxy(self)
