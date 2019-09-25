### Day1 住房贷款 图表2 ###

import matplotlib.pyplot as plt
import matplotlib as mpl                        # 中文字体设置
mpl.rcParams['font.sans-serif'] = ['SimHei']    #设置简黑字体

A = 4000000     #总贷款额
Y = 10          #贷款年份
C = C1 = 0      #等额本息、等额本金总还款
B = B1 = 0      #等额本息、等额本金总利息  
R = 0.06        #年利率 
m = R/12        #月利率
n = 12*Y        #总还款期数
d = A/n         #等额本金每月本金还款

title = str(int(A/10000)) +'万贷款'+str(Y)+'年 年利率'+str(int(R*100))+'% 每月还款额示意图'
plt.title(title)
plt.xlabel('月份')
plt.ylabel('每月还款金额 （元）')
plt.grid(linestyle='-.', axis='y') #只显示y轴网格线

#print("### 等额本息",Y,"年 ###")     #等额本息
#x = A*m*pow(1+m,n) / (pow(1+m,n)-1)  

pic_x = [i for i in range(1,12*Y+1)] # 总月份
pic_y = [A*m*pow(1+m,n)/(pow(1+m,n)-1) for i in range(1,12*Y+1)] # 万元

#print("### 等额本金",Y,"年 ###")     #等额本金
pic_y1 = []
for i in range(1,n+1) :
    x = d + (A-(i-1)*d)*m
    pic_y1.append(x)

plt.plot(pic_x,pic_y,'.',label='等额本息')
plt.plot(pic_x,pic_y1,'.',label='等额本金')
plt.legend()                  #显示标签
plt.show()
