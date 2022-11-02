# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:54:10 2022

@author: 王宇彤

"""

#%% Exercise4.1 
import turtle
import math
import polygon.py
t=turtle.Turtle()

def arc(t,r,angle):
    """
    r:radius
    """
    arc_length = 2*math.pi*r*abs(angle)/360
    n = int(arc_length/4)+3
    step_length = arc_length/n
    step_angle = float(angle)/n
    t.lt(step_angle/2)
    polygon.polyline(t,n,step_length,step_angle)
    t.rt(step_angle/2)

"""
该函数通过增加多边形的边数去逼近圆，但函数第一笔为直线，
在乌龟画出第一笔前先左转一定角度以进行修正
"""
    


#%% Exercise4.2

import turtle
import math

t=turtle.Turtle()

def arc(t,r,angle):  
      
      c = 2*math.pi*r  
      n =int(c/3)+1
      length = 2*c/n
      n1 = int(n*(angle/360))
      for i in range(n1):
          t.fd(length)
          t.lt(360/n)

        
t=turtle.Turtle()
def petal(t,r,angle):
      c = 2*math.pi*r   
      n =int(c/3)+1 
      length = 2*c/n
      n1 = int(n*(angle/360))
      for i in range(2):
          for i in range(n1):       
              t.fd(length)
              t.lt(360/n)
          t.lt(180-angle)
          
def flower(t,r,angle,n):
    """n 为花瓣个数"""
    b = 360/n #花瓣夹角
    for i in range(n):
        t.lt(b)
        petal(t,r,angle)
        

flower(t,100,60,6)




#%%4.3
import turtle
import math
t =turtle.Turtle()

def umberlla(t,n,l):  
    a = 360/n
    a_out =(180+a)/2
    l_out =2*math.sin(math.radians(a/2))*l
    
    for i in range(n):
        t.lt(a*i)
        t.fd(l)
        t.lt(a_out)
        t.fd(l_out)
        t.home()
        t.pd()

umberlla(t,7,60)
    

#%%4.5

import turtle
import math

t = turtle.Turtle()

def Archi_spiral(t,a,b,n):
    theta = 0 
    d_theta = 3
    r = a+b*theta
    for i in range(n):
        theta += d_theta
        r+= math.radians(d_theta)*b
        x= r*math.cos(math.radians(theta))
        y = r*math.sin(math.radians(theta))
        t.goto(x,y)

Archi_spiral(t,0,8,240)
        
        
        
    
   
    
    
    
        






   
    
        
        
    
    



 



