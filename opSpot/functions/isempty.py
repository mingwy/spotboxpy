# -*- coding: utf-8 -*-
"""
ISEMPTY True for empty operator.

Created on Mon Jul 15 13:18:31 2013

@author: User
"""

def isempty(A):
    if A.m == 0 or A.n == 0:
        return True
    else:
        return False
