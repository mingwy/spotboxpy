# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:00:28 2013

@author: User
"""

def isspot(A):
    from opSpot import OpSpot
    return issubclass(type(A),OpSpot)