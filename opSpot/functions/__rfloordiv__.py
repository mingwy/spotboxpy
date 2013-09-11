# -*- coding: utf-8 -*-
"""
FLOORDIV(//)    Left matrix divide.

Created on Tue Sep 10 23:21:52 2013

@author: User
"""
import numpy as np
import scipy.linalg as sci

def __rfloordiv__(A,B):    
    if np.isscalar(B):
        x = (1.0/B) * A
    else:    
        if B.shape[0] != A.m:
            raise Exception ('Matrix dimensions must agree.')
            return
                
        if not A.isreal() or np.iscomplex(B).any():
            x = np.zeros((B.shape[1],A.n),dtype=complex)
        else:
            x = np.zeros((B.shape[1],A.n))
                
        ej = np.zeros((A.n,1))
        for i in range(A.n):
            ej[i] = 1
            Aej = np.dot(A,ej)
            y = sci.lstsq(B,Aej)
            y = y[0]
            x[:,i] = y[:,0]
            ej[i] = 0
    
    return x
        