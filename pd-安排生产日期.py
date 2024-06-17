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

df = pd.read_excel('用Knime 安排生产日期 V2.xlsx')

df['品类'] = df['品类/产品'].str[0]

df['累加数量']= df.groupby('品类').cumcount()
df['辅助列'] = df.groupby('品类').cumcount() // df['该品类每天可排单数量']
df['排产日期'] = df['生产时间（ 开始）'] + pd.to_timedelta(df['辅助列'], unit='D')
# 把'该品类每天可排单数量'列重命名为数量
df = df.rename(columns={'该品类每天可排单数量': '数量'})

print(df[['品类', '生产时间（ 开始）', '数量', '累加数量', '辅助列', '排产日期']])
df.drop('辅助列', axis=1, inplace=True)
print(df)

