# -*- coding: utf-8 -*-
'''

'''

from control.userControl import UserControl
from flask import Blueprint, g, session
import flask

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['POST'])
def login():

    userContrl = UserControl(requestargs=g.args, session=session)

    return flask.jsonify(userContrl.login())


@user.route('/logout', methods=['POST'])
def logout():

    userContrl = UserControl(requestargs=g.args, session=session)
    return flask.jsonify(userContrl.logout())

