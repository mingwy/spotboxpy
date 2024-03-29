# -*- coding: utf-8 -*-
"""
OPMATRIX    Convert a numeric matrix into a Spot Operator

Created on Thu Jul 18 15:25:28 2013

@author: User
"""
import numpy as np
import scipy.linalg as sci
from opSpot.opSpot import OpSpot
from opSpot.isnumeric import isnumeric

class OpMatrix(OpSpot):
    def __new__(subtype,A,description='Matrix'):
        if not isnumeric(A):
            raise Exception ('Input argument must be numeric.')
            return
        
        if np.isscalar(A):
            m = 1
            n = 1
        else:
            m = np.size(A,0)
            n = int(np.size(A)/m)
        op = OpSpot.__new__(subtype,description,m,n,A)
        op.cflag = not np.isreal(A).all()
        op.sweepflag = True
        op.matrix = A
        op.disp()
        return op
        
    def __array_finalize__(self, op):
        if op is None: 
            return
        self.matrix = getattr(op,'matrix',None)
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
        if self.isscalar():
            v = self.matrix
            string = str(v)
        else:
            string = super(OpMatrix,self).char()
        return string
            
    def double(self):
        return self.matrix
        
    def multiply(self,x,mode):
        if np.isscalar(self.matrix):
            y = self.matrix * x
        else:
            if mode == 1:
                y = np.dot(self.matrix,x)
            else:
                y = np.dot(self.matrix.conj().T,x)
        
        return y
        
    def divide(self,b,mode):
        if mode == 1:
            y = sci.lstsq(self.matrix,b)
        else:
            y = sci.lstsq(self.matrix.conj().T,b)
        
        return y[0]