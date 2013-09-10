# -*- coding: utf-8 -*-
"""
MUL    Multiplication of operator.

Created on Thu Jul 18 12:05:18 2013

@author: User
"""
import numpy as np

def __mul__(A,B):
    from spotboxpy.opFoG import OpFoG
    from spotboxpy.opSpot.isspot import isspot
    
    if not isspot(B):
        if np.isscalar(B):
            if A.n != 1:
                y = OpFoG(A,B)
            else:
                y = A.applyMultiply(B,1)
        else:
            p = np.size(B,0)
            if A.n != p:
                if A.isscalar():
                    pass
                else:
                    raise Exception ('Matrix dimensions must agress when multiplying')
                    return
            
            if A.isempty():
                y = np.zeros((A.m,np.size(B,1)))
            else:
                y = A.applyMultiply(B,1)
    else:
        y = OpFoG(A,B)
        
    return y