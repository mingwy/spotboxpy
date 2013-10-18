# -*- coding: utf-8 -*-
"""
OPBINARY   Binary (0/1) ensemble.

Created on Fri Sep 06 21:42:46 2013

@author: User
"""
import numpy as np
from opSpot.opSpot import OpSpot

class OpBinary(OpSpot):
    def __new__(subtype,m,n=None):
        if n is None:
            n = m

        op = OpSpot.__new__(subtype,'Binary',m,n,np.random.randint(2,size=(m,n)))
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
        
        
    def multiply(self,x,mode):
        if mode == 1:
            y = np.dot(self.double(),x)
        else:
            y = np.dot(self.double().conj().T,x)
            
        return y