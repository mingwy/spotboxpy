# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:55:40 2013

@author: User
"""
import numpy as np

def __pow__(A,B):
    from spotboxpy.opPower import OpPower
    from spotboxpy.opSpot.isnumeric import isnumeric
    from spotboxpy.opSpot.isspot import isspot
    
    if A.m != A.n:
        raise Exception ('Operator must be square')
        return
    
    if isspot(B):
        if B.isscalar():
            return OpPower(A,int(B))
    elif isnumeric(B):
        if not np.isscalar(B):
            raise Exception ('Exponent must be a scalar.')
            return
        else:
            return OpPower(A,B)
    else:
        raise Exception ('Invalid parameters to mpower.')
            
            
            