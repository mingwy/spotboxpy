# -*- coding: utf-8 -*-
"""
RSUB    Right-side subtraction of operator.

Created on Tue Sep 10 00:11:05 2013

@author: User
"""
import numpy as np

def __rsub__(A,B):
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

    return OpMinus(B,A)