# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:40:52 2013

@author: User
"""
import numpy as np
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.disp import disp
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot
from spotboxpy.opMatrix import OpMatrix

class OpReal(OpSpot):
    def __new__(subtype,A):
        if isnumeric(A):
            A = OpMatrix(A)
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
        
        op = OpSpot.__new__(subtype,'Real',A.m,A.n,A.real)
        op.cflag = False
        op.linear = A.linear
        op.sweepflag = A.sweepflag
        op.children.append(A)
        op.precedence = 1
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
        
        
    def char(self):
        op1 = self.children[0]
        string = 'Real(%s)' %(op1.char())
        return string
        
    def multiply(self,x,mode):
        op1 = self.children[0]
        if np.isreal(x):
            # Purely real
            y = np.real(op1.applyMultiply(x,mode))
        elif np.isreal(np.sqrt(-1)*x):
            # Purely imaginary
            y = np.real(op1.applyMultiply(np.imag(x),mode)) * np.sqrt(-1)
        else:
            # Mixed
            y = np.real(op1.applyMultiply(np.real(x),mode)) + np.real(op1.applyMultiply(np.imag(x),mode)) * np.sqrt(-1)
            
        return y

        