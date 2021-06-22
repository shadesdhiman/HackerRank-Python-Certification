# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:18:58 2021

@author: Dhiman
"""
import math

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b
        
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return math.pi*self.r*self.r