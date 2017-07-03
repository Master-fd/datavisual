# -*- coding: utf-8 -*-
'''

'''

from flask import Flask, request, g
import os
import logging
from viewhandler.page_blueprint import page

logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.context_processor
def common():
    return {'title' : u'你不懂'}


'所有蓝图'
BLUEPRINTS = [
    page
]


def bootstrap(app):
    '''
    引导启动一个app
    :param app:
    :return:
    '''

    '设置时区'
    os.environ["TZ"] = "GMT-08"

    '注册蓝图'
    for view in BLUEPRINTS:
        app.register_blueprint(view)


    @app.before_request
    def get_all_args():
        '获取请求参数'
        args = {k:v[0] for k,v in dict(request.args).items()}
        args_form = {k:v[0] for k,v in dict(request.form).items()}
        args.update(args_form)
        g.args = args



    @app.after_request
    def after_request(response):

        cors_origins = ['http://seed-dev.oa.com']
        if request.referrer:
            # 允许前端跨域请求域名
            for origin in cors_origins:
                if request.referrer.count(origin) > 0:
                    response.headers.add('Access-Control-Allow-Origin', origin)
                    break

        response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Credentials, Methods")
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response





bootstrap(app)



if __name__ == '__main__':


    logging.info('run open_data_platform host:{}:{}'.format(app.config['APP_HOST'], app.config['APP_PORT']))
    logging.info('run mode:{}'.format(app.config['DEBUG']))
    app.run(host=app.config['APP_HOST'], port=app.config['APP_PORT'], debug=app.config['DEBUG'])



