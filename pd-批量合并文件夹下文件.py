# -*- coding: utf-8 -*-
# @Time : 2023/8/20 18:02
# @Author : 瑜亮
# @FileName : pd-批量合并文件夹下文件.py

import pandas as pd

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('colheader_justify', 'center')


import pathlib  

 
folder = pathlib.Path.cwd().parent.joinpath(r'路径')  
 
filenames = [fp.name for fp in folder.iterdir() if fp.match('*.dat')]  # 获取所有 .dat 文件的文件名  
 
dfs = []  # 存储所有 DataFrame 的列表  
index = 0  # 文件名索引变量  
for fp in folder.iterdir():  # 迭代文件夹  
    if fp.match('*.dat'):  # re 正则匹配判断文件夹里是否有 csv 文件  
        df = pd.read_csv(fp, header=None, encoding='utf-8', sep='|')  # 添加文件，转为 pandas 的 DataFrame  
        df['Filename'] = filenames[index]  # 将文件名添加到 DataFrame 中  
        dfs.append(df)  # 将 DataFrame 添加到列表中  
        index += 1  # 更新索引变量  
 
# 使用 pandas.concat() 函数将多个 DataFrame 合并成一个  
merged_df = pd.concat(dfs, axis='index', ignore_index=True)
print(merged_df)


