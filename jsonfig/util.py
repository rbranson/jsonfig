class DictionaryProxy(object):
    def __init__(self, func=dict):
        self._f = func
 
    def __getitem__(self, name):
        return self._f().__getitem__(name)
 
    def __setitem__(self, name, value):
        return self._f().__setitem__(name, value)
 
    def __getattr__(self, name):
        return getattr(self._f(), name)
