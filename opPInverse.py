# -*- coding: utf-8 -*-
"""
OPPINVERSE  Pseudo inverse of operator.

Created on Tue Jul 23 15:34:13 2013

@author: User
"""
import scipy.linalg as sci
from opMatrix import OpMatrix
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.disp import disp
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot

class OpPInverse(OpSpot):
    def __new__(subtype,A):
        if isnumeric(A):
            A = OpMatrix(A)
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
            
        op = OpSpot.__new__(subtype,'PInverse',A.n,A.m,sci.pinv(A))
        op.cflag = A.cflag
        op.linear = A.linear
        op.sweepflag = A.sweepflag
        op.children.append(A)
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
        string = self.children[0].char()
        string = string.join(('pinv(',')'))
        return string
        
    def multiply(self,x,mode):
        if mode == 1:
            A = self.children[0]
        else:
            A = self.children[0].conj().T
            
        y = sci.lstsq(A,x)
        return y[0]
            