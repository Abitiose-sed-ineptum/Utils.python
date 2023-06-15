# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:44:08 2022

@author: jason
"""

# Helful functions to do circuit analysis

class CircuitUtils:
    
    def __init__(self):
        pass
    
    def voltageDivider(self, v_src, r_eq, r_load):        
        return v_src * (r_load/r_eq)
    
    def currentDivider(self, i_src, r_eq, r_load):
        return i_src * (r_eq/r_load)