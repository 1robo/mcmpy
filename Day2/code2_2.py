### Day2 曲线拟合 回归分析 ###
import matplotlib.pyplot as plt 
import numpy as np
# 通用字体设置
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体

plt.grid(linestyle='-.')
title = '酵母菌数量增长模型'
plt.title(title)
plt.xlabel('时间 (小时）')
plt.ylabel('酵母菌生物量')

time = [i for i in range(0,19)]
number = [9.6,18.3,29,47.2,71.1,119.1,174.6,257.3,\
          350.7,441.0,513.3,559.7,594.8,629.4,640.8,\
          651.1,655.9,659.6,661.8]


fit = np.polyfit(time,number,1) #按一阶多项式拟合
print(fit) #输出各项系数
P = np.poly1d(fit)
print(P) #输出方程式


plt.plot(time,number,'o',label='实际测量值')
plt.plot(time,P(time),label='拟合曲线')
plt.legend() 
plt.show()

