# -*- coding: utf-8 -*-
'''

'''


from flask import Blueprint, url_for, render_template, render_template_string

page = Blueprint('page', __name__, url_prefix='/page')




@page.route('/index/')
def page_view():
    data= {
           'name' : True,
           'data' : [1,2,3]}
    return render_template('page1.html', **data)



@page.route('/main/')
def page_main():
    data= {
           'name' : True,
           'data' : [1,2,3]}
    return render_template('main.html')












