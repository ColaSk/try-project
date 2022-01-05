import weakref
from logging import getLogger

_log = getLogger(__name__)

class Extension(object):
    
    __params = None
    container = None

    def __new__(cls, *args, **kwargs):
        """clone params"""
        inst = super().__new__(cls)
        inst.__params = (args, kwargs)
        return inst
    
    def clone(self):
        if self.is_bound():
            raise RuntimeError('Cannot `bind` a bound extension.')
        cls = type(self)
        args, kwargs = self.__params
        instance = cls(*args, **kwargs)
        return instance

    def bind(self, container):
        """ Get an instance of this Extension to bind to `container`.
        """
        instance = self.clone()
        instance.container = weakref.proxy(container) # Weak reference
        return instance

    def is_bound(self):
        return self.container is not None


def is_extension(obj):
    return isinstance(obj, Extension)
