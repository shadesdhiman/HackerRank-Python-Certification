# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:53:30 2021

@author: Dhiman
"""

class Car:

    def __new__(self, max_speed,unit):
        self.max_speed = max_speed
        self.unit = unit
        return "Car with the maximum speed of "+ str(self.max_speed) + " " + self.unit

class Boat:

    def __new__(self,max_speed):
        return "Boat with the maximum speed of "+ str(self.max_speed) + " knots"