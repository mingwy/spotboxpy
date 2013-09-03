# -*- coding: utf-8 -*-
"""
CHAR    Create a string representation of a Spot operator.

Created on Tue Jul 02 16:38:14 2013

@author: User
"""

def char(A):
    m = A.m
    n = A.n
    t = A.optype
    string = '%s(%d,%d)' %(t,m,n)
    return string
    