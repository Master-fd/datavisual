# -*- coding: utf-8 -*-
'''

'''
import redis


def Connection(host, port):

    pool = redis.ConnectionPool(host=host, port=port)
    redis_tmp = redis.Redis(connection_pool=pool)
    redis_db = redis_tmp

    return redis_db





