# -*- coding: utf-8 -*-
'''

'''



from connect import db_redis,  db_mysql
from logger import logger



class BaseModel(object):

    redis_db = db_redis.Connection(host=config.REDIS_HOST, port=config.REDIS_PORT)
    pg_old_db = db_postgresql.Connection(host=config.PG_DB_OLD_HOST, port=config.PG_DB_OLD_PORT, user=config.PG_DB_OLD_USER, password=config.PG_DB_OLD_PSWD, database=config.PG_DB_OLD_NAME, is_return_res=False)   #旧的GPV, user info信息数据库
    mysql_db = db_mysql.Connection(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER, password=config.MYSQL_PASSWD, database=config.MYSQL_DB, charset='utf8', is_return_res=False)

    def __init__(self, fbusiness_id=None):

        self.redis_timeout = 60*60*24  #缓存时间


    '专门用于生成redis的key'
    @classmethod
    def get_redis_key(cls, prefix=None, key=None):
        '''
        根据前缀和key，组合生成对应的redis key, 例如 o_user:+4091 =  o_user:4091
        :return: str
        '''
        if not prefix or not isinstance(prefix, str):
            raise Exception('prefix must str')
        key = str(key)
        return prefix+key

    def redis_set(self, name=None, value=None, ex=None):
        '默认cache24 h'
        if not name or not value:
            return False
        if not ex:
            ex = self.redis_timeout
        if self.redis_db:
            logger.info('设置redis值--key:{}--value:{}--expire:{}'.format(name, value, ex))
            self.redis_db.set(name, value)
            self.redis_db.expire(name, ex)
            return True
        else:
            return False

    def redis_get(self, name):
        '从redis中获取'
        if not name:
            return None
        if self.redis_db:
            data = self.redis_db.get(name)
            logger.info('从redis读--key:{}--value:{}'.format(name, data))
            return data
        else:
            return None


    '专门用于批量删除key, 例如删除以test开头的key 则 test* '
    @classmethod
    def delete_redis_keys(cls, pattern=None):

        if not pattern:
            return False
        keys = cls.redis_db.keys(pattern=pattern)
        if keys:
            cls.redis_db.delete(*keys)
        return True




if __name__ == '__main__':


    db = BaseModel(fbusiness_id=3)