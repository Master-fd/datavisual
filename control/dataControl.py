# -*- coding: utf-8 -*-
'''

'''


from baseControl import BaseControl
from collections import defaultdict

class DataContral(BaseControl):


    def format_data(self, dims=None):

        data = dims.get('data', [])
        name = dims.get('name', '')
        dict_data = defaultdict(list)
        for item in data:     #转成{ {'2017-05-16': [11, 2]}, {'2017-05-17': [110, 2]}} 格式
            key = item.get('fdate', None)
            dict_data[key].append(item.get(name))

        axis_x = []
        axis_y = []
        temp = sorted(dict_data.items(), key=lambda x:x[0], reverse=False)   #依据key来升序排序, 趋势表，key就是时间
        for key, obj_list in temp:
            axis_x.append(key)
            data = sum([num for num in obj_list if isinstance(num, (float, int, long))])  #对值进行求和
            axis_y.append(data)

        dims = {
            'series': {
                'name' : name,
                'data' : axis_y
            },
            'xAxis' : axis_x
        }
        return dims


    def get_data(self):

        # data = {
        #     'xAxis' : ["06-26", "06-27", "06-28", "06-29", "06-30"],
        #     'series' :[{'type': "bar", 'name': "付费总额", 'data': [22.62, 25.72, 27.61, 21.56, 26.14]},
        #             {'type': "line",  'name': "ARPU", 'data': [20, 23, 21, 26, 12]}
        #     ],
        #     'title' : "显示测试"
        # }

        dims = {
            'data' : [{'fdate' : '2017-02-01', 'ARPU':10}, {'fdate' : '2017-02-02', 'ARPU':12}, {'fdate' : '2017-02-03', 'ARPU':13}, {'fdate' : '2017-02-04', 'ARPU':15}],
            'name' : 'ARPU'
        }
        data = self.format_data(dims)
        data['title'] = '测试'
        print data
        return self.responseJson(self.ErrorCode.SUCCESS, data=data)




