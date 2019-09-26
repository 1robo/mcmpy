### Day1 住房贷款 图表1 ###

import matplotlib.pyplot as plt
import matplotlib as mpl                      # 通用字体设置
mpl.rcParams['font.sans-serif'] = ['SimHei']  #设置简黑字体

A = 4000000     #总贷款额
Y = 10          #贷款年份
C = C1 = 0      #等额本息、等额本金总还款
B = B1 = 0      #等额本息、等额本金总利息  
R = 0.06        #年利率 
m = R/12        #月利率
n = 12*Y        #总还款期数
d = A/n         #等额本金每月本金还款

title = str(A) + '万贷款 年利率'+str(int(R*100))+'% 总还款额示意图'
plt.title(title)
plt.xlabel('贷款年份')
plt.ylabel('总还款额（万元）')
plt.grid(linestyle='-.')

#print("### 等额本息",Y,"年 ###")     #等额本息
#C = A*R*Y*pow(1+m,n) / (pow(1+m,n)-1)

#print("### 等额本金",Y,"年 ###")     #等额本金 
#C1 = A*(2+m*n+m)/2

A = int(A/10000)                #贷款400万
pic_x = [1,5,10,15,20,25,30]    # 年份
pic_y = [A*R*i*pow(1+m,i*12)/(pow(1+m,i*12)-1) for i in pic_x] # 万元
pic_y1= [A*(2+m*i*12+m)/2 for i in pic_x]

plt.plot(pic_x,pic_y,label='等额本息')
plt.plot(pic_x,pic_y1,label='等额本金')
plt.legend()                  #显示标签
plt.show()
