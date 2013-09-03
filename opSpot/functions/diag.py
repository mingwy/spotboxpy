# -*- coding: utf-8 -*-
"""
DIAG    Diagonal operator and diagonals of an operator.

Created on Mon Jul 15 15:57:24 2013

@author: User
"""
import numpy as np
from size import size

def diag(A):
    p = size(A)
    k = np.amin(p)
    d = np.zeros((k,1))
    for i in range(k):
        v = np.zeros((p[1],1))
        v[i] = 1
        w = np.dot(A,v)
        d[i] = w[i]
        
    return d
    
