# -*- coding: utf-8 -*-
__author__ = 'TaurenDruid'

from __future__ import with_statement

import json

def get_setting():
    with open('config.conf') as config:
        return json.load(config)

def get_sqlite():
    config=get_setting()
    return config["Sqlite"]

def get_redis():
    config=get_setting()
    return config['RedisServer']

def get_MySQL_server():
    config=get_setting()
    return config['MySQLServer']