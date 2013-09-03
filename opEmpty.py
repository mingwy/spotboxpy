# -*- coding: utf-8 -*-
"""
OPEMPTY     Operatro equivalent as an empty matrix

Created on Mon Jul 29 15:02:59 2013

@author: User
"""
import numpy as np
from opSpot.opSpot import OpSpot

class OpEmpty(OpSpot):
    def __new__(subtype,m=0,n=0):
        if m != 0 and n != 0:
            raise Exception ('At least one dimension must be zero.')
            return
            
        op = OpSpot.__new__(subtype,'Empty',m,n)
        op.disp()
        return op
        
    def __array_finalize__(self, op):
        if op is None: 
            return
        self.optype = getattr(op,'optype',None)
        self.m = getattr(op,'m',None)
        self.n = getattr(op,'n',None)
        self.opcounter = getattr(op,'opcounter',None)
        self.linear = getattr(op,'linear',None)
        self.cflag = getattr(op,'cflag',None)
        self.children = getattr(op,'children',None)
        self.precedence = getattr(op,'precedence',None)
        self.sweepflag = getattr(op,'sweepflag',None)
        
        
    def double(self):
        A = []
        return A
        
    def multiply(self,x,mode):
        if mode == 1:
            y = np.zeros(self.m,0)
        else:
            y = np.zeros(self.n,0)
            
        return y
    
    