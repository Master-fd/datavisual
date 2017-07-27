# -*- coding: utf-8 -*-
'''

'''
from datetime import timedelta

"""
run host and port
"""
APP_HOST = 'localhost'
APP_PORT = 8000
DEBUG = True

"""
mysql 连接配置
"""
MYSQL_HOST = '119.29.151.45'
MYSQL_PORT = 3306
MYSQL_DB = 'test'
MYSQL_USER = 'root'
MYSQL_PASSWD = '633922'

"""
REDIS Database Configuration
"""
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


MONGODB_HOST = '119.29.151.45'
MONGODB_PORT = 27017
MONGODB_DB = 'mytest'

SESSION_COOKIE_NAME = 'session_id'
SECRET_KEY = '7984564451'
PERMANENT_SESSION_LIFETIME = timedelta(days=1)


ADMINS_MAIL_LIST    = ['RobotZhu@boyaa.com']
MAIL_HOST           = 'smtp.qq.com' #mail.boyaa.com'
MAIL_PORT           = '587'
MAIL_FROMADDR       = '1003768663@qq.com'  #d_alert@boyaa.com'
MAIL_USERNAME       = '1003768663@qq.com' #'d_alert'
MAIL_PASSWORD       = 'pxaxaabqpybfbecb' #'D@12!zy$34'

LOGGING_FILE = 'E:\\Project\\dc_open_data_platform\\dc_mobile.log'
