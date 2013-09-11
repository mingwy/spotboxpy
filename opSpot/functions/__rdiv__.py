# -*- coding: utf-8 -*-
"""
RDIV    Slash or right matrix divide.

Created on Tue Sep 10 22:42:32 2013

@author: User
"""
import numpy as np

def __rdiv__(A,B):  
    if np.isscalar(B):
        y = (1.0/B) * A
    else:
        if A.isscalar():
            y = A // B.conj().transpose()
        else:
            y = A.ctranspose() // B.conj().transpose()
            y = y.conj().transpose()
    
    return y