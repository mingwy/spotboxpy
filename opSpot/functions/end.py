# -*- coding: utf-8 -*-
"""
END returns maximum index

Created on Wed Jul 03 15:50:59 2013

@author: User
"""
from size import size

def end(A,k,idxcount):
    m,n = size(A,nargout=2)
    if idxcount == 1:
        e = m*n
    else:
        if k == 1:
            e = m-1
        elif k == 2:
            e = n-1
        else:
            e = 0
            
    return e
            