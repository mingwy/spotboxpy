# -*- coding: utf-8 -*-
"""
RMUL    Right-side multiplication of operator.

Created on Mon Sep 09 23:37:04 2013

@author: User
"""
import numpy as np

def __rmul__(A,B):
    from spotboxpy.opFoG import OpFoG
    
    if np.isscalar(B) and A.m != 1:
        y = OpFoG(B,A)
    else:
        y = np.dot(A.double().conj().T,B.conj().T)
        y = y.conj().T

    return y