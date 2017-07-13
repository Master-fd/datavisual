# -*- coding: utf-8 -*-
'''

'''

import paramiko
import sys, os, random
import datetime
from datetime import timedelta


class ShellExec(object):

    host = '192.168.0.94'
    port = 3600
    user = 'hadoop'
    pkey = '/home/hadoop/.ssh/id_rsa'

    def __init__(self):
        self._connect()

    def _connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        self.ssh.connect(self.host, self.port, self.user, self.pkey)

    def execute(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read(), stderr.read()


def insert_user(level=None, count=10):



    lines = []
    for i in range(1, count):
        row = '{workid},{name},{level}\n'.format(workid=i, name='user_' + level+'_'+str(i), level=level)
        lines.append(row)

    with open('user.txt', 'a+') as fd:
        fd.writelines(lines)

def insert_level():
    row1 = '{level},{auth}\n'.format(level='manager', auth=4)
    row2 = '{level},{auth}\n'.format(level='CTO', auth=3)
    row3 = '{level},{auth}\n'.format(level='leader', auth=2)
    row4 = '{level},{auth}\n'.format(level='staff', auth=1)
    row5 = '{level},{auth}\n'.format(level='PM', auth=2)
    row6 = '{level},{auth}\n'.format(level='CEO', auth=5)
    row7 = '{level},{auth}\n'.format(level='COO', auth=3)

    with open('level.txt', 'a+') as fd:
        fd.writelines([row1, row2, row3, row4, row5, row6, row7])

def insert_gameid():
    #'gameid,gamename'

    row1 = '{},{}\n'.format(1, '斗地主')
    row2 = '{},{}\n'.format(2, '麻将')
    row3 = '{},{}\n'.format(3, '扑克')
    row4 = '{},{}\n'.format(4, '斗牛')

    with open('game.txt', 'a+') as fd:
        fd.writelines([row1, row2, row3, row4])


def insert_data(delta=0, sta=1, end=100):

    date = (datetime.datetime.now().date()-timedelta(days=delta)).strftime('%Y-%m-%d')

    game_id=[1,2,3,4]
    all = []
    for i in range(sta, end):
        #date,userid,gameid
        row = '{},{},{}\n'.format(date, i, random.choice(game_id))
        all.append(row)

    with open('usergame8.txt', 'a+') as fd:
        fd.writelines(all)






if __name__ == '__main__':


    # insert_gameid()
    insert_data(1, 50, 200)