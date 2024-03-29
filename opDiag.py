# -*- coding: utf-8 -*-
"""
OPDIAG   Diagonal operator.

Created on Tue Aug 27 17:16:09 2013

@author: User
"""
import numpy as np
import scipy.sparse as sparse
import scipy.linalg as linalg
from opSpot.opSpot import OpSpot

class OpDiag(OpSpot):
    def __new__(subtype,D):
        D = D.flatten(1)
        n = np.size(D)
        diag = sparse.spdiags(D,0,n,n).toarray()
        op = OpSpot.__new__(subtype,'Diag',n,n,diag)
        op.cflag = not np.isreal(D).all()
        op.sweepflag = True
        op.diag = diag
        op.disp()
        return op
        
    def __array_finalize__(self, op):
        if op is None: 
            return
        self.diag = getattr(op,'diag',None)
        self.optype = getattr(op,'optype',None)
        self.m = getattr(op,'m',None)
        self.n = getattr(op,'n',None)
        self.opcounter = getattr(op,'opcounter',None)
        self.linear = getattr(op,'linear',None)
        self.cflag = getattr(op,'cflag',None)
        self.children = getattr(op,'children',None)
        self.precedence = getattr(op,'precedence',None)
        self.sweepflag = getattr(op,'sweepflag',None)
        
        
    def multiply(self,x,mode):
        if mode == 1:
            y = np.dot(self.diag,x)
        else:
            y = np.dot(self.diag.conj().T,x)
        
        return y
        
    def divide(self,x,mode):
        if mode == 1:
            y = linalg.lstsq(self.diag,x)
        else:
            y = linalg.lstsq(self.diag.conj().T,x)
        
        return y[0]
