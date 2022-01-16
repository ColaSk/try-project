# -*- encoding: utf-8 -*-
'''
@File    :   entrypoints.py
@Time    :   2022/01/04 18:54:06
@Author  :   sk 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

import inspect
import types
from functools import partial
from .extensions import Extension
from try_framework.config import gl

def register_entrypoint(fn, entrypoint):
    descriptors = getattr(fn, gl.ENTRYPOINT_EXTENSIONS_ATTR, None)
    if descriptors is None:
        descriptors = set()
        setattr(fn, gl.ENTRYPOINT_EXTENSIONS_ATTR, descriptors)
    descriptors.add(entrypoint)

class Entrypoint(Extension):

    method_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def bind(self, container, method_name):
        """ Get an instance of this Entrypoint to bind to `container` with
        `method_name`.
        """
        instance = super().bind(container)
        instance.method_name = method_name
        return instance

    @classmethod
    def decorator(cls, *args, **kwargs):
        """Registered entrance decorator"""

        def registering_decorator(fn, args, kwargs):
            instance = cls(*args, **kwargs)
            register_entrypoint(fn, instance)
            return fn

        if len(args) == 1 and isinstance(args[0], types.FunctionType):
            return registering_decorator(args[0], args=(), kwargs={})
        else:
            return partial(registering_decorator, args=args, kwargs=kwargs)
