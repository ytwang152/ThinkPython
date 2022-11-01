# -*- coding: utf-8 -*-
"""

Created on Thu Oct 20 18:27:08 2022
@author: 王宇彤
"""

#Exercise2.1
print("Exercise2.1")
# 42 = n
print("42 = n是不合法的，首先，变量名不能为纯数字或以数字开头；其次，如果把n作为值赋给某变量，需要先对n赋值")
# x = y = 1
print("x = y = 1是合法的，相当于先将1赋给y，再将y赋给x。")
# x = 1; n = 2
# y = x+n;
print("分号在python中代表语句的结束，也可以用换行代替。")
# y = 1.
# y = "hello".
# print(1).
print("period在编程中代表属性访问符，放在函数语句和赋值语句中会报错，但若放在纯数字赋值中不会报错（没查到为什么）。")
# x = 1; y = 1; print(xy)
print("计算机会将xy识别为一个新变量，如果想让两者相乘，应在中间加运算符。")

#Exercise2.2
import math
print("2.2.1   ","半径为5的球体积为",4/3*math.pi*5**3)
print("2.2.2   ","60本书的总价为",(24.95*0.6+0.75)*60+(3-0.75))

seconds_0 = (6*60+52)*60
seconds_1 = (8*60+15)*2+(7*60+12)*3+seconds_0
m,s = divmod(seconds_1,60)
h,m = divmod(m,60)
print("2.2.3   ""回家吃饭的时间是","%02d:%02d:%02d" % (h,m,s))





