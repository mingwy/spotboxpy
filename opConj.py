# -*- coding: utf-8 -*-
"""
OPCONJ  Take the elementwise conjugate of a complex operator

Created on Mon Jul 15 12:14:10 2013

@author: User
"""
from opMatrix import OpMatrix
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot

class OpConj(OpSpot):
    def __new__(subtype,A):
        if isnumeric(A):
            A = OpMatrix(A)
        
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
        
        op = OpSpot.__new__(subtype,'Conj',A.m,A.n,A.conj())
        op.cflag = A.cflag
        op.linear = A.linear
        op.sweepflag = A.sweepflag
        op.children.append(A)
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
        string = op1.char()
        string = string.join(('Conj(',')'))
        return string
        
    def multiply(self,x,mode):
        if mode == 1:
            y = self.children[0].applyMultiply(x.conj(),1).conj()
        else:
            y = self.children[0].applyMultiply(x.conj(),2).conj()
        
        return y
