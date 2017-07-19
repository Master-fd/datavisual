# -*- coding: utf-8 -*-
'''

'''

from flasktest.control.userControl import UserControl
from flask import Blueprint
import flask

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['POST'])
def login():

    userContrl = UserControl()
    return flask.jsonify(userContrl.login())


@user.route('/logout', methods=['POST'])
def logout():
    userContrl = UserControl()
    return flask.jsonify(userContrl.logout())

