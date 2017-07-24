# -*- coding: utf-8 -*-
'''

'''
from common.reponse import Responses, ErrorCode


class BaseControl(object):


    def __init__(self, requestargs={}, session=None):

        self.args = requestargs
        self.session = session
        self.ErrorCode = ErrorCode


    def responseJson(self, code=0, data={}, msg=''):

        return Responses.responseJson(code=code, data=data, msg=msg)

