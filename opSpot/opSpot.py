# -*- coding: utf-8 -*-
"""
opSpot    Spot operator super class.

Created on Fri Jul 05 16:10:14 2013

@author: User
"""
import numpy as np
from spotboxpy.opSpot.size import size
from spotboxpy.opSpot.isscalar import isscalar
from spotboxpy.opSpot.char import char
from spotboxpy.spot.counter import Counter

class OpSpot(np.ndarray):
    def __new__(subtype,optype=None,m=0,n=0,input_arr=None):
        m = np.maximum(0,m)
        n = np.maximum(0,n)
        if np.round(m) != m or np.round(n) != n:
            print 'Warning: Size parameters are not integer.'
            m = np.floor(m)
            n = np.floor(n)
            
        if input_arr is None:
            op = np.ndarray.__new__(subtype,shape=(m,n))
        else:
            op = np.asarray(input_arr).view(subtype)
            
        op.optype = optype
        op.m = m
        op.n = n 
        op.opcounter = Counter()
        op.linear = 1    
        op.cflag = False
        op.children = []
        op.precedence = 1
        op.sweepflag = False
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

          
    def getNprods(self):
        nprods = np.array([self.opcounter.mode1,self.opcounter.mode2])
        return nprods
        
    def applyMultiply(self,x,mode):
        if self.opcounter.plus1(mode) == 0:
            return
            
        if self.sweepflag:
            y = self.multiply(x,mode)
        else:
            q = size(x,2)
            if q > 1:
                if isscalar(self):
                    y = np.ndarray.__new__(type(x),size(x))
                    y.fill(0)
                elif mode == 1:
                    y = np.ndarray.__new__(type(x),(self.m,q))
                    y.fill(0)
                else:
                    y = np.ndarray.__new__(type(x),(self.n,q))
                    y.fill(0)
            for i in range(q):
                y[:,i] = self.multiply(x[:,i],mode)
        
        return y
        
    def applyDivide(self,x,mode):
        y = self.divide(x,mode)
        return y
        
    char = char
    