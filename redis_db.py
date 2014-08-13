__author__ = 'lihongchao'

import redis
from  readconfig import  ReadConfig
class RedisDB():
    def __init__(self):
        rc = ReadConfig()
        redis = rc.ReadSection('redis')
        self.host= redis['host']
        self.port =  redis['port']
        self.db_index = redis['db_index']

        if self.host is None:
            self.host='127.0.0.1'
        if self.port is None:
            self.port = 6379
        if self.db_index is None:
            self.db_index = 12

    def connect(self):
        self.rs=redis.StrictRedis(host=self.host,port=self.port,db=self.db_index)
        return self.rs

if __name__=="__main__":
    rdb=RedisDB()
    rs=rdb.connect()
    rs.set("aaa","1231221")
    print rs.get("aaass")
    rs.save()