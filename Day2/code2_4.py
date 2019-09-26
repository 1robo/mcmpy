# 随堂练习  读取excel 表格
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
# 通用字体设置
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体

plt.grid(linestyle='-.')
title = '机器数量与商品产量关系'
plt.title(title)
plt.xlabel('机器数量 (台）')
plt.ylabel('每天生产商品（万个)')


df = pd.read_excel('work.xlsx')

table =df.loc[:,['MACHINE','PRODUCT']].values

m = []
p = []
for i in range(len(table)) :
    m.append(table[i][0])
    p.append(table[i][1])

fit = np.polyfit(m,p,1)   #按一阶多项式拟合
print(fit)                #输出各项系数
F = np.poly1d(fit)
print(F)                #输出方程式

print(round(F(6)))             #6台机器产量
print(round(F(25)))            #25台机器产量

m1 = [i for i in range(0,30)]
p1 = F(m1)
plt.plot(m,p,'o',label='实际测量值')
plt.plot(m1,p1,label='拟合曲线')
plt.plot([6,25],[F(6),F(25)],'o',label='预测值')

plt.legend() 
plt.show()

