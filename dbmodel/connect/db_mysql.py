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
    def __init__(self, host, port, database, user, password, charset, is_return_res=False):

        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.is_return_res = is_return_res


    def query_one_dict(self, sql=None, params=None):
        '''
        获取单行数据，返回字典
        :return: dict
        '''
        datas, exe_res, msg = self.execute_query(sql=sql, params=params)
        if self.is_return_res:
            if len(datas) >= 1:
                return datas[0], exe_res, msg
            else:
                return {}, exe_res, msg
        else:
            return datas[0] if datas else {}


    def query_list(self, sql=None, params=None):
        '''
        获取多行数据，返回list
        :param sql: str
        :return: list
        '''
        datas, exe_res, msg =  self.execute_query(sql=sql, params=params)
        if self.is_return_res:
            return datas, exe_res, msg
        else:
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
                if is_return:
                    cursor.execute('select LAST_INSERT_ID() as id') #返回自增id
                    temp = cursor.fetchone()
                else:
                    temp = {}
            conn.commit()
            if self.is_return_res:
                return temp, True, '执行成功' if is_return else True, True, '执行成功'
            else:
                return temp if is_return else True
        except Exception as e:
            logger.error('''MYSQL_SQL 执行失败-{}
                            SQL 语句 -- {}'''.format(e, sql))
            conn.rollback()
            if self.is_return_res:
                return {}, False, '执行异常--{}'.format(e)if is_return else False, False, '执行异常'
            else:
                return {} if is_return else False
        finally:
            conn.close()

    def execute_commit_list(self, sql_list=None):
        """
        执行多条sql 比如update, insert, delete等操作
        """
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.database, charset=self.charset, cursorclass=pymysql.cursors.DictCursor)  #建立连接
        try:

            if not isinstance(sql_list, (tuple, list)):
                sql_list = [sql_list]

            record_sql = None
            with conn.cursor() as cursor:
                for sql in sql_list:
                    logger.info('MYSQL_SQL = {}'.format(sql))
                    record_sql = sql
                    cursor.execute(sql)
            conn.commit()
            return True, True, '执行成功' if self.is_return_res else True
        except Exception as e:
            logger.error('''MYSQL_SQL 执行失败-{}
                            SQL 语句 -- {}'''.format(e, record_sql))
            conn.rollback()
            return False, False, '执行异常--{}'.format(e) if self.is_return_res else False
        finally:
            conn.close()  #关闭连接

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
            if len(datalist)>50: #查询的数据太长了，不要打印log，方便查看
                logger.info('MYSQL_SQL 查询结果长度{} 显示缩略版 = {}'.format(len(datalist), datalist[0]))
            else:
                logger.info('MYSQL_SQL 查询结果 = {}'.format(datalist))

            return list(datalist), True, 'SQL执行成功'
        except Exception as e:
            conn.rollback()
            logger.error('''MYSQL_SQL 执行失败 - {}
                            SQL 语句 -- {}'''.format(e, sql))
            return [], False, 'SQL执行异常--{}'.format(e)
        finally:
            conn.close()





