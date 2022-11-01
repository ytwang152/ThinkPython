# -*- coding: utf-8 -*-
"""

Created on Wed Oct 19 19:09:55 2022
@author: 王宇彤
"""



#Exercise1.1.1#
# print('Hello,world'
#print"Hello,world"
print("1.1.1  ","漏掉一个扩号或两个括号，均会显示SyntaxError，语法错误。")
  
#Exercise1.1.2#
# print('Hello,world)
# print(Hello,world)
print("1.1.2  ","漏掉一个引号，在运行时会显示SyntaxError，为语法错误；  \
      漏掉两个，会显示NameError，若文本类字符未加引号打印，计算机会将其识别为变量，在此之前应对其赋值。")

#Exercise1.1.3#
# print(2++2)   
print("1.1.3  ","++仍被识别为+。")

#Exercise1.1.4#
# print(07)
print("1.1.4  ""直接在数字前加入leading zeros是非法的，因为可能会导致歧义，计算机不能确定数字在何种进位制下。")


#Exercise1.1.5#
print(24)
print("1.1.5  ","如果没有运算符，会直接被识别为一个新值。")

#Exercise1.2#
import math
print("Exercise1.2")
print("总秒数：",42*60+42)# 总秒数： 2562
print("英里数：",10/1.61)# 英里数： 6.211180124223602
seconds = 42*60+42
average_pace = seconds/(10/1.61)
m,s = divmod(average_pace,60)
print("平均配速为","%02d分%02d秒" %(m,s))
print("平均速度：",10/1.61/(42+42/60)*60,"英里/时")# 平均速度： 8.727653570337614 英里/时











    


    
        
           






