# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:41:19 2013

@author: User
"""
import numpy as np 

def isposintmat(m):
    return all(np.around(m) == m) and all(m >= 0)