### Day2 线性拟合 回归分析 ###
import matplotlib.pyplot as plt 
import numpy as np
# 通用字体设置
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False # 解决‘-’bug
plt.grid(linestyle='-.')
title = '弹簧伸长与所吊重物质量之间关系模型'
plt.title(title)
plt.xlabel('弹簧所吊重物质量 (克)')
plt.ylabel('弹簧伸长（厘米）')

M = [ 50*i for i in range(1,12)] #列表解析表达式
L = [6.005,6.879,7.750,8.252,9.370,9.872,10.675,11.502,12.365,13.120,13.805]
F = np.polyfit(M,L,1) #按一阶多项式拟合
print(F) #输出各项系数
P = np.poly1d(F)
print(P) #输出方程式

print(P(600))	#输出重量为600g的长度


M_New = M + [50*i for i in range(12,15)]  #延长 x 轴
plt.plot(M,L,'o',label='实际测量值')
plt.plot(M_New,P(M_New),label='拟合曲线')

plt.plot(600,P(600),'o',label='预测值')
plt.legend() 
plt.show()
