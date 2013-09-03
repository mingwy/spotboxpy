# -*- coding: utf-8 -*-
"""
CTRANSPOSE  Complex conjugate transpose.
Created on Mon Jul 15 15:54:38 2013

@author: User
"""

def ctranspose(A):
    from spotboxpy.opCTranspose import OpCTranspose
    return OpCTranspose(A)
