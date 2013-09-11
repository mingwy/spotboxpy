# -*- coding: utf-8 -*-
"""
FLOORDIV(//)    Left matrix divide.

Created on Wed Jul 17 15:25:05 2013

@author: User
"""
import numpy as np

def __floordiv__(A,B):
    from spotboxpy.opSpot.isspot import isspot
         
    if not isspot(B):
        if np.isscalar(B):
            rowB = 1
            colB = 1
        else:
            rowB = B.shape[0]
            colB = B.shape[1]

        if A.m != rowB:
            raise Exception ('Matrix dimensions must agree.')
            return
            
        if not A.isreal() or np.iscomplex(B).any():
            x = np.zeros((A.n,colB),dtype=complex)
        else:
            x = np.zeros((A.n,colB))
            
        if np.isscalar(B):
            x = A.divide(B,1)
        else:
            for i in range(np.size(B,1)):
                x[:,i] = A.divide(B[:,i],1)
            
    else:
        x = A.pinv() * B
        
    return x
                