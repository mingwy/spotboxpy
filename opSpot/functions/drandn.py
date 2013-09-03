# -*- coding: utf-8 -*-
"""
DRANDN      Normally distributed pseudorandom vector in the operator domain

Created on Wed Jul 17 15:15:31 2013

@author: User
"""
import numpy as np
from isreal import isreal

def drandn(A):
    x = np.random.randn(A.n,1)
    if isreal(A):
        return x
    else:
        return x + 1j*x
