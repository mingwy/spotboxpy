# -*- coding: utf-8 -*-
"""
OPEYE   Identity operator.

Created on Tue Jul 23 16:36:37 2013

@author: User
"""
import numpy as np
from opSpot.opSpot import OpSpot

class OpEye(OpSpot):
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
            
        op = OpSpot.__new__(subtype,'Eye',m,n,np.eye(m,n))
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
        A = np.eye(self.m,self.n)
        return A
        
    def multiply(self,x,mode):
        m = self.m
        n = self.n
        if mode == 1:
            if m <= n:
                y = x[0:m-1]
            else:
                y = np.hstack([x,np.zeros((m-n,1))])
        else:
            if n <= m:
                y = x[0:n-1]
            else:
                y = np.hstack([x,np.zeros((n-m,1))])
                
        return y