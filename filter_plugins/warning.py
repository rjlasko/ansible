#!/usr/bin/env python

from ansible.utils.display import Display


class FilterModule(object):
    """
    see: https://stackoverflow.com/a/56420339/4027379
    """
    def filters(self):
        return {'warn_custom': self.warn_filter}

    def warn_filter(self, message, **kwargs):
        Display().warning(message)
        return message
