# -*- coding: utf-8 -*-
"""
OPTRANSPOSE   Transpose of an operator.

Created on Tue Aug 27 17:00:19 2013

@author: User
"""
from opConj import OpConj
from opCTranspose import OpCTranspose
from opMatrix import OpMatrix
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.disp import disp
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot

class OpTranspose(OpSpot):
    def __new__(subtype,A):
        if isnumeric(A):
            A = OpMatrix(A)
        
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
        
        op = OpSpot.__new__(subtype,'Transpose',A.n,A.m,A.T)
        op.cflag = A.cflag
        op.linear = A.linear
        op.sweepflag = A.sweepflag
        op.children.append(A)
        op.opIntrnl = OpCTranspose(OpConj(A))
        disp(op)
        return op
        
    def __array_finalize__(self, op):
        if op is None: 
            return
        self.opIntrnl = getattr(op,'opIntrnl',None)
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
        string = op1.char()
        if op1.precedence > self.precedence:
            string = string.join('(',')')
        string = string + ".'"
        return string
        
    def multiply(self,x,mode):
        y = self.opIntrnl.applyMultiply(x,mode)
        return y

