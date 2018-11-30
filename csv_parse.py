# -*- coding: utf-8 -*-
import json
import pandas as pd
import numpy as np
import re

def csv_parse(df):
    with open(source_file, encoding='utf-8') as f:
        for r in f.readlines():
            data_dict = json.loads(r)


if __name__ == '__main__':
    with open('test.txt', encoding='utf-8') as f:
        for r in f.readlines():
            print(r)
            local = re.search(r'【坐标】：(.*)【兴趣标签】', r).group(1)
            print(local)
