# -*- coding: utf-8 -*-
"""
OPPOWER   Raise operator to integer power.

Created on Wed Aug 28 17:01:20 2013

@author: User
"""
import numpy as np
from opMatrix import OpMatrix
from opSpot.opSpot import OpSpot
from opSpot.isnumeric import isnumeric
from opSpot.isspot import isspot

class OpPower(OpSpot):
    def __new__(subtype,A,p):
        if np.round(p) != p:
            raise Exception('Second argument to opPower must be an integer.')
            return
        
        if isnumeric(A):
            A = OpMatrix(A)
        
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
            
        if A.m != A.n:
            raise Exception ('Warning: Operator is not a square matrix.')
            return
            
        op = OpSpot.__new__(subtype,'Power',A.m,A.m,np.linalg.matrix_power(A,p))
        op.cflag = A.cflag
        op.linear = A.linear
        op.children.append(A)
        op.exponent = p
        
        if p == 0:
           fun = lambda op,x,mode: x
        elif p > 0:
            fun = lambda op,x,mode: op.opPower_intrnl(x,mode)
        else:
            y = np.linalg.inv(np.linalg.matrix_power(A,np.abs(p)))
            fun = lambda op,x,mode: y.applyMultiply(x,mode)
        op.funHandle = fun
           
        op.disp()
        return op
        
    def __array_finalize__(self, op):
        if op is None: 
            return
        self.exponent = getattr(op,'exponent',None)
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
        
        
    def char(self):
        string = self.children[0].char()
        p = str(self.exponent)
        string = '^'.join((string,p))
        return string
        
    def multiply(self,x,mode):
        y = self.funHandle(self,x,mode)
        return y
        
    def opPower_intrnl(self,x,mode):
        y = x
        for i in range(self.exponent):
            y = self.children[0].applyMultiply(y,mode)
            
        return y