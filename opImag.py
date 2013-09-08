# -*- coding: utf-8 -*-
"""
OPIMAG   Complex imaginary part of operator.

Created on Sat Sep 07 22:19:43 2013

@author: User
"""
import numpy as np
from opMatrix import OpMatrix
from opSpot.opSpot import OpSpot
from opSpot.isnumeric import isnumeric
from opSpot.isspot import isspot

class OpImag(OpSpot):
    def __new__(subtype,A):
        if isnumeric(A):
            A = OpMatrix(A)
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
        
        op = OpSpot.__new__(subtype,'Imag',A.m,A.n,A.double().imag)
        op.cflag = False
        op.linear = A.linear
        op.sweepflag = A.sweepflag
        op.children.append(A)
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
        
        
    def char(self):
        op1 = self.children[0]
        string = 'Imag(%s)' %(op1.char())
        return string
        
    def multiply(self,x,mode):
        op1 = self.children[0]
        if mode == 1:
            if np.isreal(x).all():
                # Purely real
                y = np.imag(op1.applyMultiply(x,mode))
            elif np.isreal(1j*x).all():
                # Purely imaginary
                y = np.imag(op1.applyMultiply(np.imag(x),mode)) * 1j
            else:
                # Mixed
                y = np.imag(op1.applyMultiply(np.real(x),mode)) + np.imag(op1.applyMultiply(np.imag(x),mode)) * 1j
        else:
            if np.isreal(x).all():
                # Purely real
                y = np.imag(op1.applyMultiply(x,mode)) * -1
            elif np.isreal(1j*x).all():
                # Purely imaginary
                y = np.imag(op1.applyMultiply(np.imag(x),mode)) * 1j * -1
            else:
                # Mixed
                y = np.imag(op1.applyMultiply(np.real(x),mode)) * -1 + np.imag(op1.applyMultiply(np.imag(x),mode)) * 1j * -1
            
        return y

