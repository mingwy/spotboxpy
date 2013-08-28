# -*- coding: utf-8 -*-
"""
OPSUM   Addition of two operators.

Created on Mon Jul 22 12:23:00 2013

@author: User
"""
from spotboxpy.opMatrix import OpMatrix
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.disp import disp
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot

class OpSum(OpSpot):
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
        op = OpSpot.__new__(subtype,'Sum',m,n,A+B)
        op.cflag = A.cflag or B.cflag
        op.linear = A.linear or B.linear
        op.sweepflag = A.sweepflag and B.sweepflag
        op.children.append(A)
        op.children.append(B)
        op.precedence = 4
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
        op2 = self.children[1]
        string1 = op1.char()
        if op1.precedence > self.precedence:
            string1 = string1.join(('(',')'))
        string2 = op2.char()
        if op2.precedence > self.precedence:
            string2 = string2.join(('(',')'))
        
        string = ' + '.join((string1,string2))
        return string
        
    def double(self):
        A = self.children[0].double() + self.children[1].double()
        return A
        
    def multiply(self,x,mode):
        y = self.children[0].applyMultiply(x,mode)
        y = y + self.children[1].applyMultiply(x,mode)
        return y
