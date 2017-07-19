# -*- coding: utf-8 -*-
'''

'''
import flask
from flask import Blueprint
from flasktest.common.auth import auth
from flasktest.control.dataControl import DataContral

data = Blueprint('data', __name__, url_prefix='/data')



@data.route('/getdata/')
@auth.login_require
def getdata():

    datacontrol = DataContral()

    return flask.jsonify(datacontrol.get_data())

