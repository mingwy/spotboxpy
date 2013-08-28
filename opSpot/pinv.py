# -*- coding: utf-8 -*-
"""
PINV Pseudo-inverse of an operator.
Created on Tue Jul 16 15:27:53 2013

@author: User
"""
from spotboxpy.opPInverse import OpPInverse

def pinv(A):
    return OpPInverse(A)