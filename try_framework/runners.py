# -*- encoding: utf-8 -*-
'''
@File    :   runners.py
@Time    :   2022/01/04 15:31:21
@Author  :   sk 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

"""
Define services runner
"""
from .container import get_container_cls

class ServicesRunner(object):

    def __init__(self, config):

        self.config = config
        self.services_map = {}
        self.container_cls = get_container_cls(config)
    
    @property
    def service_names(self):
        return self.services_map.keys()

    @property
    def containers(self):
        return self.services_map.values()

    def add_service(self, cls):
        """ Add a service class to the runner.
        """
        container = self.container_cls(cls, self.config)
        service_name = container.service_name

        if service_name in self.services_map:
            raise Exception(f"'{service_name}' service already exists")

        self.services_map[service_name] = container

    def run_services(self, *services):
        for service in services:
            self.add_service(service)