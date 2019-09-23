### Day1 住房贷款 纯计算 ###

A = 4000000     #总贷款额
Y = 10          #贷款年份
C = C1 = 0      #等额本息、等额本金总还款
B = B1 = 0      #等额本息、等额本金总利息  
R = 0.06        #年利率 
m = R/12        #月利率
n = 12*Y        #总还款期数
d = A/n         #等额本金每月本金还款

print("### 等额本息",Y,"年 ###")     #等额本息
x = A*m*pow(1+m,n) / (pow(1+m,n)-1)  
C = A*R*Y*pow(1+m,n) / (pow(1+m,n)-1)
B = C - A
print("%.2f" % x)  
print("%.2f" % C )
print("%.2f" % B )

print("### 等额本金",Y,"年 ###")     #等额本金 
for i in range(1,n+1) :
    x = d + (A-(i-1)*d)*m 
    if i == 1 or i==n :    
        print("%.2f" % x)
C1 = A*(2+m*n+m)/2
B1 = C1 - A
print("%.2f" % C1 )
print("%.2f" % B1 )

print("### 两者比较 ###" )        #两者比较
print("%.2f" % (C-C1) )
print("%.2f" % (B-B1) )
