# -*- coding: utf-8 -*-
"""
REAL    Complex real part.

Created on Mon Jul 15 13:48:12 2013

@author: User
"""
from isreal import isreal
from spotboxpy.opReal import OpReal

def real(A):
    if isreal(A):
        pass
    else:
        A = OpReal(A)
    return A
