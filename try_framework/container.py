# -*- encoding: utf-8 -*-
'''
@File    :   container.py
@Time    :   2022/01/04 15:33:50
@Author  :   sk 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

"""
Define service core container
"""

import inspect
from .config import gl
from .utils import SpawningSet
from .extensions.extensions import iter_extensions

class ServiceContainer(object):
    
    def __init__(self, service_cls, config):

        self.service_cls = service_cls
        self.config = config
        self.entrypoints = SpawningSet()

        """Gets the sub extension of the extension, 
        which will be initialized when the container is initialized
        """
        self.subextensions = SpawningSet()

        self.init()
   
    @property
    def service_name(self):
        service_name = getattr(self.service_cls, 'name', None)
        service_name = self.service_cls.__name__ if service_name is None else service_name

        if not isinstance(service_name, str):
            raise Exception(
                'Service name attribute must be a string ({}.{}.name)'.format(
                    self.service_cls.__module__, self.service_cls.__name__))
                    
        return service_name
    
    def init(self):
        
        # rpc init
        for method_name, method in inspect.getmembers(self.service_cls, inspect.isfunction):
            entrypoints = getattr(method, gl.ENTRYPOINT_EXTENSIONS_ATTR, [])
            for entrypoint in entrypoints:
                bound = entrypoint.bind(self, method_name)
                self.entrypoints.add(bound)
                self.subextensions.update(iter_extensions(bound))
    
    # def __getattr__(self, name):
    #     pass

def get_container_cls(config):
    """
    TODO: Adapt multiple service containers
    """
    return  ServiceContainer