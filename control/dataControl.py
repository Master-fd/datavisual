# -*- coding: utf-8 -*-
'''

'''


from baseControl import BaseControl


class DataContral(BaseControl):


    def get_data(self):

        data = {
            'xAxis' : ["06-26", "06-27", "06-28", "06-29", "06-30"],
            'series' :[{'type': "bar", 'name': "付费总额", 'data': [22.62, 25.72, 27.61, 21.56, 26.14]},
                    {'type': "line",  'name': "ARPU", 'data': [20, 23, 21, 26, 12]}
            ],
            'title' : "显示测试"
        }
        return self.responseJson(self.ErrorCode.SUCCESS, data=data)




