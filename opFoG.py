# -*- coding: utf-8 -*-
"""
OPFOG   Forms the product of two operators.

Created on Wed Aug 28 15:16:12 2013

@author: User
"""
import numpy as np
from spotboxpy.opMatrix import OpMatrix
from spotboxpy.opSpot.opSpot import OpSpot
from spotboxpy.opSpot.disp import disp
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot
from spotboxpy.opSpot.isscalar import isscalar

class OpFoG(OpSpot):
    def __new__(subtype,A,B):
        if isnumeric(A):
            A = OpMatrix(A)
        if isnumeric(B):
            B = OpMatrix(B)
            
        if not (isspot(A) and isspot(B)):
            raise Exception ('One of the operators is not a valid input.')
            return
        
        if not (isscalar(A) or isscalar(B) or A.n == B.m):
            raise Exception ('Operators are not compatible in size.')
            return
            
        if isscalar(A) or isscalar(B):
            m = max(A.m,B.m)
            n = max(A.n,B.n)
        else:
            m = A.m
            n = B.n
            
        op = OpSpot.__new__(subtype,'FoG',m,n,np.dot(A,B))
        op.cflag = A.cflag or B.cflag
        op.linear = A.linear or B.linear
        op.sweepflag = A.sweepflag and B.sweepflag
        op.children.append(A)
        op.children.append(B)
        op.precedence = 3
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
        
        string = ' * '.join((string1,string2))
        return string
        
    def double(self):
        return np.dot(self.children[0].double(),self.children[1].double())
        
    def multiply(self,x,mode):
        if mode == 1:
            y = self.children[1].applyMultiply(x,mode)
            z = self.children[0].applyMultiply(y,mode)
        else:
            y = self.children[0].applyMultiply(x,mode)
            z = self.children[1].applyMultiply(y,mode)
            
        return z

