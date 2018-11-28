# -*- coding:utf8 -*-
import json
import pandas as pd
import numpy as np

def json_parse(source_file):
    
    with open(source_file, encoding='utf-8') as f:
        for r in f.readlines():
            data_dict = json.loads(r)
        
    return data_dict

if __name__ == '__main__':    

#    data_daily = './data_daily.txt'
#    data_month = './data_month.txt'
#    data_week = './data_week.txt'
    data_daily = './daily.txt'
    data_month = './month.txt'
    data_week = './week.txt'
    
    dict_d = json_parse(data_daily)
    dict_m = json_parse(data_month)
    
    
    dict_m['now']