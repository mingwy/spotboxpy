# -*- coding: utf-8 -*-
"""
OPCONJ  Take the elementwise conjugate of a complex operator

Created on Mon Jul 15 12:14:10 2013

@author: User
"""
from opMatrix import OpMatrix
from opSpot.opSpot import OpSpot
from opSpot.isnumeric import isnumeric
from opSpot.isspot import isspot

class OpConj(OpSpot):
    def __new__(subtype,A):
        if isnumeric(A):
            A = OpMatrix(A)
        
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
        
        op = OpSpot.__new__(subtype,'Conj',A.m,A.n,A.double().conj())
        op.cflag = A.cflag
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
        string = self.children[0].char()
        string = string.join(('Conj(',')'))
        return string
        
    def conj(self):
        self.children[0].disp()
        return self.children[0]
        
    def ctranspose(self):
        return self.children[0].transpose()
        
    def transpose(self):
        return self.children[0].ctranspose()
        
    def multiply(self,x,mode):
        op1 = self.children[0]
        if mode == 1:
            y = op1.applyMultiply(x.conj(),1).conj()
        else:
            y = op1.applyMultiply(x.conj(),2).conj()
        
        return y
