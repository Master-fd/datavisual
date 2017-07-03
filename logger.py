# -*- coding: utf-8 -*-
'''

'''


import logging
from logging import StreamHandler
from logging.handlers import SMTPHandler, RotatingFileHandler
import config

class LoggerConfig(object):

    def __init__(self):
        # 设置logger级别默认 info级别
        self.logger_name = 'root'

        logging.basicConfig(filename = config.LOGGING_FILE, level = logging.DEBUG)
        self.add_file_handler()
        self.add_stream_handler()
        self.add_mail_handler()


    @property
    def logger(self):
        return logging.getLogger(self.logger_name)

    def add_file_handler(self):
        file_handler = RotatingFileHandler(config.LOGGING_FILE, maxBytes=1024 * 1024 * 100, backupCount=20, delay=False)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        logging.getLogger(self.logger_name).addHandler(file_handler)


    def add_mail_handler(self):

        mail_handler = SMTPHandler(mailhost=(config.MAIL_HOST, config.MAIL_PORT),
                                   fromaddr = config.MAIL_FROMADDR,
                                   toaddrs = config.ADMINS_MAIL_LIST,
                                   subject = 'Server error',
                                   credentials = (config.MAIL_USERNAME, config.MAIL_PASSWORD), secure = ())

        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(logging.Formatter('''
                                            Message type:       %(levelname)s
                                            Location:           %(pathname)s:%(lineno)d
                                            Module:             %(module)s
                                            Function:           %(funcName)s
                                            Time:               %(asctime)s
                                            Message:
                                            %(message)s
                                            '''))
        logging.getLogger(self.logger_name).addHandler(mail_handler)


    def add_stream_handler(self):
        handler = StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        logging.getLogger(self.logger_name).addHandler(handler)


logger = LoggerConfig().logger



if __name__ == '__main__':

    logger.error('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
