# -*- coding: utf-8 -*-
'''

'''

from flask import g, session

class BaseControl(object):


    def __init__(self):

        self.args = g.args
        self.session = session
