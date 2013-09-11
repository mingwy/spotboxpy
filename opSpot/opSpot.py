# -*- coding: utf-8 -*-
"""
opSpot    Spot operator super class.

Created on Fri Jul 05 16:10:14 2013

@author: User
"""
import numpy as np
import functions as fun
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
            q = x.shape[1]
            if q > 1:
                if fun.isscalar(self):
                    y = np.ndarray.__new__(type(x),(x.shape[0],x.shape[1]))
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


import os
__dir = os.path.dirname(os.path.realpath(__file__))
__dir = list(__dir)
__dir.append('/functions')
__dir = ''.join(__dir)
for __file in os.listdir(__dir):
    if __file.endswith('.py') and __file != '__init__.py':
        __name = __file[:-3]
        __mod = getattr(fun,__name,None)
        setattr(OpSpot,__name,__mod)
        
        case1 = ['__neg__','__pos__','__rmul__','__rdiv__','__rtruediv__','__rfloordiv__','__rsub__']
        case2 = ['__div__','__truediv__','__floordiv__','__mul__','__sub__','__pow__']
        char = ['r','i']
        if '__' in __name:
            if __name in case1:
                pass
            elif __name in case2:
                __name1 = list(__name)
                __name1.insert(2,char[1])
                __name1 = ''.join(__name1)
                setattr(OpSpot,__name1,__mod)
            else:
                for i in range(2):
                    __name1 = list(__name)
                    __name1.insert(2,char[i])
                    __name1 = ''.join(__name1)
                    setattr(OpSpot,__name1,__mod)
    

    
    