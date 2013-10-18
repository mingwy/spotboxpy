# -*- coding: utf-8 -*-
"""
OPEXCISE   Excise rows or columns of an operator.

Created on Mon Jul 29 15:23:52 2013

@author: User
"""
import numpy as np
from opMatrix import OpMatrix
from opRestriction import OpRestriction
from opSpot.opSpot import OpSpot
from opSpot.isnumeric import isnumeric
from opSpot.isspot import isspot
from spot.utils.isposintmat import isposintmat

class OpExcise(OpSpot):
    def __new__(subtype,A,idx,itype):
        if isnumeric(A):
            A = OpMatrix(A)
        if not isspot(A):
            raise Exception ('Input operator is not valid.')
            return
        if itype in set(['col','cols','column','columns']):
            rowExcise = False
            dimIdx = 1
        elif itype in set(['row','rows']):
            rowExcise = True
            dimIdx = 0
        else:
            raise Exception ('Invalid parameter for operator type.')
            return
            
        if np.isscalar(idx):
            idx = np.array([idx])
            
        if idx.dtype == bool:
            if idx.size > A.size(dimIdx):
                raise Exception ('Index exceeds operator dimensions.')
                return
        elif isposintmat(idx):
            if np.max(idx) >= A.size(dimIdx):
                raise Exception ('Index exceeds operator dimensions.')
                return
        else:
            raise Exception ('Subscript indices must be either real integers >=0 or logicals')
            return
            
        if idx.dtype == bool:
            idxReverse = np.ndarray((A.size(dimIdx),1),dtype=bool)
            idxReverse.fill(True)
            idxReverse[idx] = False
        else:
            idxReverse = np.setdiff1d(np.arange(0,A.size(dimIdx)),idx)
            
        if rowExcise:
            opIntrnl = OpRestriction(A.size(0),idxReverse) * A
        else:
            opIntrnl = A * OpRestriction(A.size(1),idxReverse).ctranspose()
            
        m,n = opIntrnl.size()
        op = OpSpot.__new__(subtype,'Excise',m,n,opIntrnl.double())
        op.cflag = A.cflag
        op.linear = A.linear
        op.children.append(A)
        op.opintrnl = opIntrnl
        op.indices = idx
        op.rowexcise = rowExcise
        op.disp()
        return op
        
    def __array_finalize__(self,op):
        if op is None: 
            return
        self.opintrnl = getattr(op,'opintrnl',None)
        self.indices = getattr(op,'indices',None)
        self.rowexcise = getattr(op,'rowexcise',None)
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
        if self.rowexcise:
            itype = 'Rows'
        else:
            itype = 'Cols'
            
        string = self.children[0].char()
        string = 'Excise(%s,%s)' %(string,itype)
        return string
        
    def multiply(self,x,mode):
        y = self.opintrnl.applyMultiply(x,mode)
        return y
        
