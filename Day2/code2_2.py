# 随堂练习
import matplotlib.pyplot as plt
import numpy as np
# 通用字体设置
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体

plt.grid(linestyle='-.')
title = '工作时间与良品率关系'
plt.title(title)
plt.xlabel('时间 (小时）')
plt.ylabel('良品率 %')

X = [ i for i in range(10,20)] #列表解析表达式
Y = [45,51,54,61,66,70,74,78,85,89]

F = np.polyfit(X,Y,1)   #按一阶多项式拟合
print(F)                #输出各项系数

P = np.poly1d(F)
print(P)                #输出方程式

print(np.polyval(F,20))#输出重量为600g的长度
print(np.polyval(F,6))#输出重量为600g的长度


F1 = np.polyval(F,X)
plt.plot(X,Y,'o',label='实际测量值')
plt.plot(X,F1,label='拟合曲线')
plt.legend() 
plt.show()
