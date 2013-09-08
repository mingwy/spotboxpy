# -*- coding: utf-8 -*-
"""
IMAG Complex imaginary part

Created on Mon Jul 15 13:40:09 2013

@author: User
"""

def imag(A):
    from spotboxpy.opZeros import OpZeros
    from spotboxpy.opImag import OpImag
    if A.isreal():
        A = OpZeros(A.m,A.n)
    else:
        A = OpImag(A)
        
    return A