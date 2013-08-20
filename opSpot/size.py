# -*- coding: utf-8 -*-
"""
SIZE    Dimensions of a Spot operator

Created on Thu Jul 04 12:15:51 2013

@author: User
"""
import numpy as np

def size(A,dim=None,nargout=1):
    if dim is not None:
        if dim != 0 and dim != 1:
            print 'Dimension argument must be 0 or 1.'
            return
        else:
            if dim == 0:
                return A.m
            else:
                return A.n
    else:
        if nargout == 1:
            p = np.array([A.m,A.n])
            return p
        else:
            p = A.m
            q = A.n
            return p,q
        