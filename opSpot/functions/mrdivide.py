# -*- coding: utf-8 -*-
"""
MRDIVIDE    Slash or right matrix divide.

Created on Thu Jul 18 12:25:23 2013

@author: User
"""
import numpy as np
from spotboxpy.opSpot.isspot import isspot

def mrdivide(A,B):
    if isspot(A):
        valA =  A.isscalar()
    else:
        valA = np.isscalar(A)
    if isspot(B):
        valB =  B.isscalar()
    else:
        valB = np.isscalar(B)
        
    if valB:
        y = (1.0/B) * A
    elif valA:
        y = (1.0/A) * B
    else:
        y = np.linalg.lstsq(B.ctranspose(),A.ctranspose())
        y = y[0].ctranspose()
    
    return y