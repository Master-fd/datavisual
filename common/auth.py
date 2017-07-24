# -*- coding: utf-8 -*-
'''

'''


from common.reponse import Responses
import flask
from flask import session

class Auth():

    def login_require(self, func):

        def wrap(*args, **kwargs):

            isLogin = True if 'account' in session else False
            if not isLogin:
                return flask.jsonify(Responses.responseJson(Responses.NO_LOGIN, msg='没有登录'))

            return func(*args, **kwargs)
        return wrap


auth = Auth()

