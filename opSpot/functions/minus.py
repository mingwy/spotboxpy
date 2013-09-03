# -*- coding: utf-8 -*-
"""
Difference of two operators.

Created on Tue Jul 16 15:07:37 2013

@author: User
"""
from isscalar import isscalar
from size import size

def minus(A,B):
    from spotboxpy.opOnes import OpOnes
    from spotboxpy.opMinus import OpMinus
    if isscalar(A):
        A = OpOnes(size(B)) * A
    if isscalar(B):
        B = OpOnes(size(A)) * B

    return OpMinus(A,B)