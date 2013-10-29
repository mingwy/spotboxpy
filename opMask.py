# -*- coding: utf-8 -*-
"""
OPMASK  Selection mask.

Created on Thu Oct 03 16:48:53 2013

@author: User
"""
import numpy as np
from opSpot.opSpot import OpSpot
from spot.utils.isposintmat import isposintmat

class OpMask(OpSpot):
    def __new__(subtype,idx,n=None):
        if np.isscalar(idx):
            idx = np.array([idx])
        
        idx = idx.flatten(1)
        
        if idx.dtype == bool and n is None:
            n = idx.size
        elif n is None:
            n = np.max(idx) + 1
            
        if idx.dtype == bool:
          if idx.size > n:
              raise Exception ('Index exceeds operator dimensions.')
        elif isposintmat(idx) or idx.size == 0:
            if idx.size != 0 and np.max(idx) >= n:
                raise Exception ('Index exceeds operator dimensions.')
        else:
            raise Exception ('Subscript indices must be either real integers >= 0 or logicals.')
            
        mask = np.zeros((n,1))
        mask[idx] = 1
        A = mask * np.eye(n)
        op = OpSpot.__new__(subtype,'Mask',n,n,A)
        op.mask = mask
        op.disp()
        return op
        
    def __array_finalize__(self, op):
        if op is None: 
            return
        self.mask = getattr(op,'funHandle',None)
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
        y = self.mask * x
        return y