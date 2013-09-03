# -*- coding: utf-8 -*-
"""
RRANDN Normally distributed pseudorandom vector in the operator

Created on Mon Jul 15 14:01:48 2013

@author: User
"""
import numpy as np
from isreal import isreal

def rrandn(A):
    x = np.random.randn(A.m,1)
    if isreal(A):
        return x
    else:
        return x + 1j*x
