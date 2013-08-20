# -*- coding: utf-8 -*-
"""
ISSCALAR    True if operator is a scalar

Created on Mon Jul 08 13:26:00 2013

@author: User
"""

def isscalar(A):
    if A.m == 1 and A.n == 1:
        return True
    else:
        return False