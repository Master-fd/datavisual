# -*- coding: utf-8 -*-
'''

'''


from flask import Blueprint, url_for, render_template, render_template_string
import flask

page = Blueprint('page', __name__, url_prefix='/page')



@page.context_processor
def common_title():
    return {'title' : u'主页'}



@page.route('/main/')
def page_view():
    data= {
               'name' : True,
               'data' : [1,2,3]
            }
    return render_template('main.html', **data)



@page.route('/getdata/')
def getdata():
    data = {
        'xAxis' : ["06-26", "06-27", "06-28", "06-29", "06-30"],
        'series' :[{'type': "bar", 'name': "付费总额", 'data': [22.62, 25.72, 27.61, 21.56, 26.14]},
                {'type': "line",  'name': "ARPU", 'data': [20, 23, 21, 26, 12]}
        ],
        'title' : "显示测试"
    }
    respnse = {
        'data' : data,
        'msg' : 'success',
        'code' : 0
    }

    return flask.jsonify(respnse)













