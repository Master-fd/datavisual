# -*- coding: utf-8 -*-
'''

'''




class Responses(object):

    SUCCESS                 = 0
    ERROR                   = -1
    AUTH_FAIL               = -2
    NO_LOGIN                = -3


    @classmethod
    def responseJson(cls, code=None, data=None, msg=None):

        error_msg = {
            cls.SUCCESS : '成功',
            cls.ERROR : '失败',
            cls.AUTH_FAIL : '没有权限',
            cls.NO_LOGIN : '没有登录'
        }
        if msg is None:
            msg = error_msg.get(code, '')
        if data is None:
            data = {}

        return {
            'code' : code,
            'data' : data,
            'msg' : msg
        }



