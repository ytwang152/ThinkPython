# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:11:05 2022

@author: DELL
"""

#%%Exercise3.1

def right_justify(s):
    print(""*(70-len(s)),s)
    
print(right_justify("python"))



#%%Exercise3.2

#1.测试示例
def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")
    
do_twice(print_spam)

#2.修改do_twice
def do_twice(f,x):
    f(x)
    f(x)
#3.copy print_twice
def print_twice(bruce):
    print(bruce)
    print(bruce)
#4
do_twice(print_twice,"spam")

#5 define do_four
def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)

#%%Exercise3.3
#1
def plus():
    print("+")
def minus():
    print("+ — — — — —",end=" ")
def separtor():
    print("|          ",end=" ")
def repeat_twice(f):
    f()
    f()
def repeat_four(f):
    repeat_twice(f)
    repeat_twice(f)
def row1():
    repeat_twice(minus)
    plus()
def row2():
    repeat_twice(separtor)
    print("|")
def group():
    row1()
    repeat_four(row2)
def print_grid():
    repeat_twice(group)
    row1()
    
print_grid()

#2 4*4矩阵
def ROW1():
    repeat_four(minus)
    print("+")
def ROW2():
    repeat_four(separtor)
    print("|")
def GROUP():
    ROW1()
    repeat_four(ROW2)
def print_grid4():
    repeat_four(GROUP)
    ROW1()

print_grid4()
    


    


    
    

    
    
    
    
    
    
    
    

    
    
    
    

