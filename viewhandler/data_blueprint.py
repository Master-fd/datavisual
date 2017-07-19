# -*- coding: utf-8 -*-
'''

'''
import flask
from flask import Blueprint, g, session
from common.auth import auth
from control.dataControl import DataContral

data = Blueprint('data', __name__, url_prefix='/data')



@data.route('/getdata/')
@auth.login_require
def getdata():

    datacontrol = DataContral(requestargs=g.args, session=session)

    return flask.jsonify(datacontrol.get_data())

