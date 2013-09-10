# -*- coding: utf-8 -*-
"""
Sum of two operators.

Created on Tue Jul 16 15:22:30 2013

@author: User
"""
import numpy as np

def __add__(A,B):
    from spotboxpy.opOnes import OpOnes
    from spotboxpy.opSum import OpSum
    from spotboxpy.opSpot.isspot import isspot
    
    if A.isscalar():
        A = OpOnes(B.shape) * A
    if isspot(B):
        if B.isscalar():
            B = OpOnes(A.shape) * B
    else:
        if np.isscalar(B):
            B = OpOnes(A.shape) * B
        
    return OpSum(A,B)
