# coding=utf-8
import configparser

import os
import redis

WAREHOUSE_ID = 10056


class Redis(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.dirname(os.path.dirname(__file__)) + '/config/config.ini')
        self.host = config.get("REDIS", "host")
        self.port = eval(config.get("REDIS", "port"))
        self.password = config.get("REDIS", "password")
        self.r = self.get_conn()

    def get_conn(self):
        self.pool = redis.ConnectionPool(host=self.host,
                                         password=self.password,
                                         port=self.port,
                                         decode_responses=True)
        r = redis.Redis(connection_pool=self.pool)
        return r

    def set_redis(self, skuid, stock_value):
        s = 'stock_%d_%s' % (WAREHOUSE_ID, skuid)
        self.r.set(s, stock_value * 10000)

    def get_redis(self, skuid):
        s = 'stock_%d_%s' % (WAREHOUSE_ID, skuid)
        goodsstock = float(self.r.get(s))
        return goodsstock


if __name__ == '__main__':
    my_redis = Redis()
    print(my_redis.get_redis(17918) / 10000)
