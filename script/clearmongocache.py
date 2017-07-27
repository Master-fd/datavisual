# -*- coding: utf-8 -*-
'''

'''




from dbmodel.dbbase import BaseModel
from pymongo import ASCENDING, DESCENDING
import datetime
from logger import logger

class ClearMongodbCacheScript(BaseModel):

    def __init__(self, *args, **kwargs):
        super(ClearMongodbCacheScript, self).__init__(*args, **kwargs)

        self.maxcount = 49


    def insert_script(self):

        for j in range(10):
            fdate = (datetime.datetime.now().date() + datetime.timedelta(days=j)).strftime('%Y-%m-%d')
            for i in range(10):
                self.mongo_db.business.insert_one({"sql" : 'select a from user where f={}'.format(i), "data" : 'name_'+str(i), 'flushdate' : fdate, 'flushCount':i})


    def run_script(self):

        count = self.mongo_db.business.count()

        if count < self.maxcount:
            logger.info('数量较小--{}，无需清理 '.format(count))
            return False

        overcount = count - self.maxcount
        data = self.mongo_db.business.find().sort([('flushdate', ASCENDING), ('flushCount', ASCENDING)]).limit(overcount)
        sql_list = [item.get('sql', '') for item in data]

        self.mongo_db.business.remove({'sql' : {"$in" : sql_list}})

        return True



if __name__ == '__main__':


    db = ClearMongodbCacheScript()

    db.run_script()

