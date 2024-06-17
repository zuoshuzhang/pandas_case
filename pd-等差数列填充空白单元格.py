# -*- coding: utf-8 -*-
# @Time : 2024/2/4 09:02
# @Author : 瑜亮
# @FileName : pd-把堆叠表拆分成多个表.py
from pprint import pprint  # as print
import pandas as pd
import numpy as np

# 让打印出来的数据更漂亮
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('colheader_justify', 'left')
pd.set_option('display.unicode.ambiguous_as_wide', False)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 2000)

df = pd.read_excel('等差数列填充空白单元格.xlsx')

# 使用interpolate方法进行线性插值，并设置method为'linear'
df['列1'].interpolate(method='linear', inplace=True)
df['列1'] = df['列1'].apply(lambda x: np.round(x, 2)).convert_dtypes()

print(df)
