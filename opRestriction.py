# -*- coding: utf-8 -*-
"""
OPRESTRICTION   Restriction operator.

Created on Mon Sep 30 15:24:39 2013

@author: User
"""
import numpy as np
import scipy.sparse as sci
from opSpot.opSpot import OpSpot
from spot.utils.isposintmat import isposintmat

class OpRestriction(OpSpot):
    def __new__(subtype,n,idx):
        if np.isscalar(idx):
            idx = np.array([idx])
        
        idx = idx.flatten(1)
        
        if idx.dtype == bool:
          if idx.size > n:
              raise Exception ('Index exceeds operator dimensions.')
          else:
              m = np.sum(idx)
        elif isposintmat(idx) or idx.size == 0:
            if idx.size != 0 and np.max(idx) >= n:
                raise Exception ('Index exceeds operator dimensions.')
            else:
                m = idx.size
        else:
            raise Exception ('Subscript indices must be either real integers >= 0 or logicals.')
            
        if idx.dtype == bool or idx.size == np.unique(idx).size:
            fun = lambda x,mode: opRestriction_intrnl(n,idx,x,mode)         
        else:
            P = np.zeros((n,m))
            for i in range(idx.size):
                P[idx[i]][i] = 1
            P = sci.csr_matrix(P)    
            fun = lambda x,mode: opRestrictionP_intrnl(n,idx,P,x,mode)
            
        A = np.identity(n)
        A = A[idx]   
        op = OpSpot.__new__(subtype,'Restriction',m,n,A)
        op.funHandle = fun
        op.disp()
        return op
        
    def __array_finalize__(self, op):
        if op is None: 
            return
        self.funHandle = getattr(op,'funHandle',None)
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
        y = self.funHandle(x,mode)
        return y
        
def opRestriction_intrnl(n,idx,x,mode):
    if mode == 1:
        y = x[idx]
    else:
        y = np.zeros((n,1))
        y[idx] = x
    
    return y
    
def opRestrictionP_intrnl(n,idx,P,x,mode):
    if mode == 1:
        y = x[idx]
    else:
        y = P * x
        
    return y
