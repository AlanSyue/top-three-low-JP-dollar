# -- coding: utf-8 --
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from pylab import *
import os
import lineTool

dfs = pd.read_html('https://currencyex.doitwell.tw/tw/',encoding='utf-8')

x = dfs[1].iloc[1:2,0:1]
x = str(x).split(" ")[-1]
x_bank_sold = dfs[1].iloc[1:2,1:2]
x_bank_sold = str(x_bank_sold).split(" ")[-1]
x_online_sold = dfs[1].iloc[1:2,3:4]
x_online_sold = str(x_online_sold).split(" ")[-1]

y = dfs[1].iloc[2:3,0:1]
y = str(y).split(" ")[-1]
y_bank_sold = dfs[1].iloc[2:3,1:2]
y_bank_sold =str(y_bank_sold).split(" ")[-1]
y_online_sold = dfs[1].iloc[2:3,3:4]
y_online_sold = str(y_online_sold).split(" ")[-1]

z = dfs[1].iloc[3:4,0:1]
z = str(z).split(" ")[-1]
z_bank_sold = dfs[1].iloc[3:4,1:2]
z_bank_sold = str(z_bank_sold).split(" ")[-1]
z_online_sold = dfs[1].iloc[3:4,3:4]
z_online_sold = str(z_online_sold).split(" ")[-1]


token = "LINE Notify Token"
msg = "【本日前三低日幣匯率】\n"+"1、" +x+"\t 現金賣出："+x_bank_sold+"\t即期賣出："+x_online_sold+"\n\n2、"+y+"\t 現金賣出："+y_bank_sold+"\t即期賣出："+y_online_sold+"\n\n3、"+z+"\t 現金賣出："+z_bank_sold+"\t即期賣出："+z_online_sold
lineTool.lineNotify(token,msg)


