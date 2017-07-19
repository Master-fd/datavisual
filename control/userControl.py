# -*- coding: utf-8 -*-
'''

'''

import logging
from common.reponse import Responses
from control.baseControl import BaseControl



class UserControl(BaseControl):

    def login(self):
        account = self.args.get('account', None)
        password = self.args.get('password', None)

        logging.warning(account)
        logging.warning(password)

        if account=='123' and password=='123':
            self.session['account'] = account
            return Responses.responseJson(Responses.SUCCESS)
        else:
            return Responses.responseJson(Responses.ERROR)

    def logout(self):
        self.session.pop('account', None)
        return Responses.responseJson(Responses.SUCCESS)


if __name__ == '__main__':

    db = UserControl()
    db.login()

