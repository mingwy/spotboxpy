# -*- coding: utf-8 -*-
"""
PINV Pseudo-inverse of an operator.
Created on Tue Jul 16 15:27:53 2013

@author: User
"""

def pinv(A):
    from spotboxpy.opPInverse import OpPInverse
    return OpPInverse(A)