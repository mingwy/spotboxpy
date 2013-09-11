# -*- coding: utf-8 -*-
"""
DIV    Slash or right matrix divide.

Created on Thu Jul 18 12:25:23 2013

@author: User
"""
import numpy as np

def __div__(A,B):
    if A.isscalar():
        y = (1.0/A.double()) * B
    else:
        if np.isscalar(B):
            y = B // A.ctranspose()
        else:
            y = B.conj().transpose() // A.ctranspose()
            y = y.conj().transpose()
    
    return y