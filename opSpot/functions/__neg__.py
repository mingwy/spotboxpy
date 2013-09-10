# -*- coding: utf-8 -*-
"""
Unary minus.
-A  negates the operator A.

Created on Tue Jul 16 15:43:01 2013

@author: User
"""

def __neg__(A):
    from spotboxpy.opUnaryMinus import OpUnaryMinus
    return OpUnaryMinus(A)
