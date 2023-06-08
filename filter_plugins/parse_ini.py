#!/usr/bin/env python

import configparser
import io


def from_ini(ini_str):
    config_object = configparser.ConfigParser()
    config_object.read_file(io.StringIO(ini_str))

    output = {}
    for section in config_object.sections():
        items = [(k, v.strip('"')) for k, v in config_object.items(section)]
        output[section] = dict(items)

    return output


class FilterModule(object):
    def filters(self):
        return {
            'from_ini': from_ini
        }
