# -*- coding: utf-8 -*-
'''

'''

# -*- coding: utf-8 -*-
'''
mysql 操作
'''

from pymysql.cursors import DictCursor
from logger import logger
import pymysql

class Connection(object):
    '''
    host : 主机
    port ： 端口
    database ： 数据库
    user ： 用户名
    password ： 密码
    timeout : sql执行超时时间
    '''
    def __init__(self, host, port, database, user, password, charset):

        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset


    def query_one_dict(self, sql=None, params=None):
        '''
        获取单行数据，返回字典
        :return: dict
        '''
        datas = self.execute_query(sql=sql, params=params)
        if datas:
            return datas[0]
        else:
            return {}


    def query_list(self, sql=None, params=None):
        '''
        获取多行数据，返回list
        :param sql: str
        :return: list
        '''
        datas =  self.execute_query(sql=sql, params=params)
        return datas

    def execute_commit(self, sql=None, is_return=False):
        """
        执行一条sql 比如update, insert, delete等操作
        """
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.database, charset=self.charset, cursorclass=pymysql.cursors.DictCursor)  #建立连接
        try:
            logger.info('MYSQL_SQL = {}'.format(sql))
            with conn.cursor() as cursor:
                cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            logger.error('''MYSQL_SQL 执行失败-{}
                            SQL 语句 -- {}'''.format(e, sql))
            conn.rollback()
            return False
        finally:
            conn.close()

    def execute_query(self, sql=None, params=None):
        '''
        执行一条select 类型的sql语句，
        :param sql: str
        :return:  tuple, 里面每一个为字典
        '''

        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.database, charset=self.charset, cursorclass=pymysql.cursors.DictCursor)  #建立连接

        try:
            logger.info('sql = {}'.format(sql))
            logger.info('params = {}'.format(params))

            with conn.cursor() as cursor:
                if params:  #带参数执行
                    cursor.execute(sql, params)
                else:  #不带参数，直接执行sql
                    cursor.execute(sql)
                datalist = cursor.fetchall()

            return list(datalist)
        except Exception as e:
            conn.rollback()
            logger.error('''MYSQL_SQL 执行失败 - {}
                            SQL 语句 -- {}'''.format(e, sql))
            return []
        finally:
            conn.close()





