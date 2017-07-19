# -*- coding: utf-8 -*-
'''

'''


from flask import Blueprint, url_for, render_template, render_template_string
import flask


page = Blueprint('page', __name__, url_prefix='/page')



@page.context_processor
def common_title():
    return {
        'title' : u'主页'
    }



@page.route('/main/')
def page_view():
    data= {
               'name' : True,
               'data' : [1,2,3]
            }
    return render_template('main.html', **data)














