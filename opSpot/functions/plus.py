# -*- coding: utf-8 -*-
"""
Sum of two operators.

Created on Tue Jul 16 15:22:30 2013

@author: User
"""
from isscalar import isscalar
from size import size

def plus(A,B):
    from spotboxpy.opOnes import OpOnes
    from spotboxpy.opSum import OpSum
    if isscalar(A):
        A = OpOnes(size(B)) * A
    if isscalar(B):
        B = OpOnes(size(A)) * B
        
    return OpSum(A,B)
