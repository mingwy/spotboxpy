# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:00:28 2013

@author: User
"""
from opSpot import OpSpot

def isspot(A):
    return issubclass(type(A),OpSpot)