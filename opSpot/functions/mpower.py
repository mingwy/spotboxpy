# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:55:40 2013

@author: User
"""
import numpy as np
from spotboxpy.opSpot.isnumeric import isnumeric
from spotboxpy.opSpot.isspot import isspot

def mpower(A,B):
    from spotboxpy.opPower import OpPower
    if np.size(A,0) != np.size(A,1):
        raise Exception ('Operator must be square')
        return
    if not np.isscalar(B):
        raise Exception ('Exponent must be a scalar.')
        return
    
    if not isspot(A) and isnumeric(A):
        return np.linalg.matrix_power(A,B)
    elif isspot(A):
        return OpPower(A,B)
    else:
        raise Exception ('Invalid parameters to mpower.')
            
            
            