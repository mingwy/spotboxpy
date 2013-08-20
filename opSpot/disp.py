# -*- coding: utf-8 -*-
"""
DISP    Display a Spot operator

Created on Wed Jul 17 14:32:32 2013

@author: User
"""

def disp(A,name=None):
    if A.linear == 1:
        lin = 'yes'
    else:
        lin = 'no'
    if A.cflag:
        cf = 'yes'
    else:
        cf = 'no'
        
    if name is not None:
        print '%s = ' %(name)
    print 'Spot Operator:  %s' %(A.char())
    print ' rows: %d   complex: %s\n cols: %d   type: %s' %(A.m,cf,A.n,A.optype)