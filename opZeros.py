# -*- coding: utf-8 -*-
"""
OPZEROS Operator equivalent to zero function

Created on Fri Jul 05 15:57:59 2013

@author: User
"""
import numpy as np
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.disp import disp
from spotboxpy.opSpot.size import size

class OpZeros(OpSpot):
    def __new__(subtype,m=None,n=None):
        if m is None and n is None:
            m = 1
            n = 1
        elif np.size(m) == 1 and n is None:
            n = m
        elif np.size(m) == 1 and np.size(n) == 1:
            pass
        elif np.size(m) == 2:
            if np.size(m,0) == 2:
                n = m[1]
                m = m[0]
            elif np.size(m,1) == 2:
                n = m[0,1]
                m = m[0,0]
        else:
            raise Exception('Too many input arguments.')
            return
            
        op = OpSpot.__new__(subtype,'Zeros',m,n)
        op.fill(0)
        op.sweepflag = True
        disp(op)
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
        A = np.zeros((size(self)))
        return A
        
    def multiply(self,x,mode):
        if mode == 1:
            s = self.m
        else:
            s = self.n
        
        if np.isinf(x).any() or np.isnan(x).any():
            y = np.dot(np.ones((s,1)),np.nan)
        else:
            y = np.zeros((s,1))
        
        return y
        