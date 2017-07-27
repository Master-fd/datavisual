# -*- coding: utf-8 -*-
'''

'''


from dbbase import BaseModel
import datetime


class DataModel(BaseModel):


    def get_data(self):

        sql = 'select id, name, level from score limit 2'

        # sql, data, flushdate, flushCount
        params = {
            'sql' : sql
        }
        res = self.mongo_db.business.find_one(params)
        if res is None:  #没有数据
            print 'use mysql'
            data = self.mysql_db.query_list(sql)

            #缓存
            params = {
                'sql' : sql,
                'data' : data,
                'flushdate' : datetime.datetime.now().date().strftime('%Y-%m-%d'),
                'flushCount' : 0
            }
            self.mongo_db.business.insert_one(params)
        else:
            print 'use mongodb'
            #刷新数据
            data = res.get('data', [])
            self.mongo_db.business.update(params, {"$inc": {'flushCount': 1}, "$set" : {'flushdate' : datetime.datetime.now().date().strftime('%Y-%m-%d')}})

        print data





if __name__ == '__main__':

    db = DataModel()
    db.get_data()