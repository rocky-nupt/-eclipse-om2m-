#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
从第三方api获得数据
（由于没有真实的数据来源，因此用已经处理好的假数据替代）
'''

data1 = {
    'name': '南京',
    'weather': [
        {
            'state': [1, 6, 6, 2, 1, 1, 7],
            'date': '2017-02-24',
            'air': [28, 20, 17, 25, 28, 27, 25],
            'windspeed': [3, 1, 2, 3, 2, 1, 1],
            'winddirection': [135, 1, 178, 111, 114, 210, 220],
        },
        {
            'state': [2, 6, 7, 2, 2, 2, 7],
            'date': '2017-02-25',
            'air': [31, 22, 18, 25, 31, 30, 26],
            'windspeed': [22, 6, 6, 11, 16, 22, 11],
            'winddirection': [189, 100, 178, 180, 186, 190, 198],
        },
        {
            'state': [3, 6, 6, 2, 3, 3, 7],
            'date': '2017-02-26',
            'air': [25, 19, 16, 23, 25, 24, 21],
            'windspeed': [18, 9, 11, 13, 18, 18, 13],
            'winddirection': [200, 190, 187, 210, 215, 220, 100],
        },
        {
            'state': [4, 7, 7, 4, 4, 4, 7],
            'date': '2017-02-27',
            'air': [24, 18, 15, 22, 24, 23, 19],
            'windspeed': [36, 10, 11, 18, 26, 36, 18],
            'winddirection': [5, 350, 1, 6, 2, 8, 15],
        },
        {
            'state': [5, 7, 7, 5, 5, 5, 6],
            'date': '2017-02-28',
            'air': [22, 19, 16, 21, 22, 20, 16],
            'windspeed': [40, 18, 19, 25, 29, 40, 25],
            'winddirection': [265, 250, 260, 265, 270, 280, 237],
        }
    ]
}

data2 = {
    'name': '杭州',
    'weather': [
        {
            'state': [3, 7, 7, 3, 3, 4, 6],
            'date': '2017-02-24',
            'air': [20, 14, 16, 19, 20, 17, 12],
            'windspeed': [25, 15, 20, 25, 25, 22, 23],
            'winddirection': [135, 1, 178, 111, 114, 210, 220],
        },
        {
            'state': [4, 7, 6, 3, 4, 4, 7],
            'date': '2017-02-25',
            'air': [18, 13, 14, 17, 18, 16, 14],
            'windspeed': [35, 14, 18, 28, 35, 30, 18],
            'winddirection': [5, 350, 1, 6, 2, 8, 15],
        },
        {
            'state': [4, 7, 7, 3, 4, 3, 6],
            'date': '2017-02-26',
            'air': [19, 14, 14, 17, 19, 17, 15],
            'windspeed': [20, 6, 6, 11, 16, 20, 15],
            'winddirection': [189, 100, 178, 180, 186, 190, 198],
        },
        {
            'state': [5, 7, 7, 4, 5, 5, 7],
            'date': '2017-02-27',
            'air': [17, 13, 15, 16, 17, 16, 11],
            'windspeed': [18, 9, 11, 13, 18, 18, 13],
            'winddirection': [200, 190, 187, 210, 215, 220, 100],
        },
        {
            'state': [2, 6, 6, 2, 3, 2, 6],
            'date': '2017-02-28',
            'air': [19, 14, 16, 17, 19, 18, 14],
            'windspeed': [40, 18, 19, 25, 29, 40, 25],
            'winddirection': [265, 250, 260, 265, 270, 280, 237],
        }
    ]
}