# -*- coding: utf-8 -*-
"""
OPORTHOGONAL    Abstract class for orthogonal operators.

Created on Mon Jul 08 17:08:03 2013

@author: User
"""
import numpy as np
from opSpot.opSpot import OpSpot

class OpOrthogonal(OpSpot):
    def __new__(subtype,optype,m=0,n=0,input_arr=None):
        op = OpSpot.__new__(subtype,optype,m,n,input_arr)
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
    
    
    def mldivide(self,b):
        x = np.dot(self.ctranspose(),b)
        return x