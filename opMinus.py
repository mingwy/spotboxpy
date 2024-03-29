# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:54:13 2013

@author: User
"""
from opMatrix import OpMatrix
from opSpot.opSpot import OpSpot
from opSpot.isnumeric import isnumeric
from opSpot.isspot import isspot

class OpMinus(OpSpot):
    def __new__(subtype,A,B):
        if isnumeric(A):
            A = OpMatrix(A)
        if isnumeric(B):
            B = OpMatrix(B)
            
        if not (isspot(A) and isspot(B)):
            raise Exception ('One of the operators is not a valid input.')
            return
        
        if not (A.m == B.m and A.n == B.n):
            raise Exception ('Operators are not compatible in size.')
            return
            
        m = A.m
        n = A.n
        op = OpSpot.__new__(subtype,'Minus',m,n,A.double()-B.double())
        op.cflag = A.cflag or B.cflag
        op.linear = A.linear or B.linear
        op.sweepflag = A.sweepflag and B.sweepflag
        op.children.append(A)
        op.children.append(B)
        op.precedence = 4
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
        op2 = self.children[1]
        string1 = op1.char()
        if op1.precedence > self.precedence:
            string1 = string1.join(('(',')'))
        string2 = op2.char()
        if op2.precedence > self.precedence:
            string2 = string2.join(('(',')'))

        string = ' - '.join((string1,string2))
        return string
        
    def multiply(self,x,mode):
        y = self.children[0].applyMultiply(x,mode)
        y = y - self.children[1].applyMultiply(x,mode)
        return y