# -*- coding: utf-8 -*-
"""
SUB     Subtraction of operator.

Created on Tue Jul 16 15:07:37 2013

@author: User
"""
import numpy as np

def __sub__(A,B):
    from spotboxpy.opOnes import OpOnes
    from spotboxpy.opMinus import OpMinus
    from spotboxpy.opSpot.isspot import isspot
    
    if A.isscalar():
        A = OpOnes(B.shape) * A
    if isspot(B):
        if B.isscalar():
            B = OpOnes(A.shape) * B
    else:
        if np.isscalar(B):
            B = OpOnes(A.shape) * B

    return OpMinus(A,B)