# -*- coding: utf-8 -*-
"""
INV Inverse of a linear operator.
Created on Mon Jul 15 13:44:30 2013

@author: User
"""

def inv(A):
    from spotboxpy.opInverse import OpInverse
    return OpInverse(A)
