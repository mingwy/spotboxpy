# -*- coding: utf-8 -*-
"""
LENGTH    Maximum dimension of operator

Created on Mon Jul 15 13:22:32 2013

@author: User
"""
import numpy as np
from size import size

def length(A):
    return np.amax(size(A))