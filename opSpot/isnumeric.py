# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:54:01 2013

@author: User
"""
import numpy as np
from isspot import isspot

def isnumeric(A):
    if isspot(A):
        return False
    elif isinstance(A,np.ndarray):
        if A.dtype == object or A.dtype == bool or A.dtype == str or A.dtype == unicode:
            return False
        else:
            return True
    else:
        if isinstance(A,(int,float,long,complex)) and not isinstance(A,bool):
            return True
        else:
            return False