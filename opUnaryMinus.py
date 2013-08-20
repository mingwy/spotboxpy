# -*- coding: utf-8 -*-
"""
OPUNARYMINUS    Negation of an operator.

Created on Thu Jul 18 14:10:58 2013

@author: User
"""
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.disp import disp
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot
from spotboxpy.opMatrix import OpMatrix

class OpUnaryMinus(OpSpot):
    def __new__(subtype,A):
        if isnumeric(A):
            A = OpMatrix(A)
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
        
        op = OpSpot.__new__(subtype,'UnaryMinus',A.m,A.n,-A)
        op.cflag = A.cflag
        op.linear = A.linear
        op.children.append(A)
        op.precedence = 2
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
        s = op1.char()
        if op1.precedence > self.precedence:
            string = '(%s)' %(s)
        string = '-%s' %(s)
        return string
        
    def dobule(self):
        return -self.children[0].double()
        
    def multiply(self,x,mode):
        return -1 * self.children[0].applyMultiply(x,mode)