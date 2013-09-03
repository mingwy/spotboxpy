# -*- coding: utf-8 -*-
"""
CONJ    Elementwise conjugate of operator.

Created on Mon Jul 15 15:51:05 2013

@author: User
"""

def conj(A):
    from spotboxpy.opConj import OpConj
    return OpConj(A)
