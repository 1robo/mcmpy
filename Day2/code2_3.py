### Day2 差分方程 ###
import matplotlib.pyplot as plt 
import numpy as np
# 通用字体设置
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False     # 解决‘-’bug
plt.minorticks_on()
plt.grid(which="both")
title = '酵母菌数量增长模型'
plt.title(title)
plt.xlabel('时间 (小时）')
plt.ylabel('酵母菌生物量')

time = [i for i in range(0,19)]
number = [9.6,18.3,29,47.2,71.1,119.1,174.6,257.3,\
          350.7,441.0,513.3,559.7,594.8,629.4,640.8,\
          651.1,655.9,659.6,661.8]

pn = [9.6,18.3,29,47.2,71.1,119.1,174.6,\
      257.3,350.7,441.0,513.3,559.7,594.8,629.4,\
      640.8,651.1,655.9,659.6]     #去掉时间为18 的生物量
deltap = [8.7,10.7,18.2,23.9,48,55.5,\
          82.7,93.4,90.3,72.3,46.4,35.1,\
          34.6,11.4,10.3,4.8,3.7,2.2]     
pn = np.array(pn)
factor = pn*(666-pn)
fit = np.polyfit(factor,deltap,1)
print(fit)


plist = [0 for i in range(25)]
plist[0] = 9.6
for i in range(1,25):    
    plist[i] = 0.00081418*(666-plist[i-1])*plist[i-1] + plist[i-1]

time1 = [i for i in range(0,25)]  #延长时间轴来观察变化趋势   

plt.plot(time,number,'o',label='实际测量值')
plt.plot(time1,plist,label='差分方程曲线')
plt.legend() 
plt.show()
