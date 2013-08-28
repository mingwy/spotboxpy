# -*- coding: utf-8 -*-
"""
MRDIVIDE    Slash or right matrix divide.

Created on Thu Jul 18 12:25:23 2013

@author: User
"""
import numpy as np
import scipy.linalg as sci
from spotboxpy.opCTranspose import OpCTranspose
from isscalar import isscalar
from isspot import isspot

def mrdivide(A,B):
    if isspot(A):
        valA =  isscalar(A)
    else:
        valA = np.isscalar(A)
    if isspot(B):
        valB =  isscalar(B)
    else:
        valB = np.isscalar(B)
        
    if valB:
        y = (1.0/B) * A
    elif valA:
        y = (1.0/A) * B
    else:
        y = sci.lstsq(B.conj().T,A.conj().T)
        y = OpCTranspose(y[0])
    
    return y