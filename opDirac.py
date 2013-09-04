# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:11:24 2013

@author: User
"""
import numpy as np
from opOrthogonal import OpOrthogonal

class OpDirac(OpOrthogonal):
    def __new__(subtype,n=1):
        op = OpOrthogonal.__new__(subtype,'Dirac',n,n,np.eye(n))
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
        
        
    def dobule(self):
        return np.eye(self.n)
        
    def multiply(self,x,mode):
        return x
