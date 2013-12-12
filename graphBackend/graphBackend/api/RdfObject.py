__author__ = 'mpetyx'

# We need a generic object to shove data in/get data from.
# Riak generally just tosses around dictionaries, so we'll lightly
# wrap that.
class RdfObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data

