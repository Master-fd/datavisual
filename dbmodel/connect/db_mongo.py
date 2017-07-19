# -*- coding: utf-8 -*-
'''

'''

from pymongo import MongoClient



class Connection(object):


    def __init__(self,host, port, database):

        self.host = host
        self.database = database
        self.port = port
        self.conn = MongoClient(host=self.host, port=self.port)
        self.mongo = eval('self.conn.'+database)








if __name__ == '__main__':

    db = Connection('119.29.151.45', 27017, 'test')


    print db.mongo.name

    print db.mongo





