# -*- coding: utf-8 -*-
'''

'''

from pymongo import MongoClient


def Connection(host, port, database):

    conn = MongoClient(host=host, port=port)
    mongo = eval('conn.'+database)
    return mongo







if __name__ == '__main__':

    db = Connection('119.29.151.45', 27017, 'my456test')


    print db.name






