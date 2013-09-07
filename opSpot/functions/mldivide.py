# -*- coding: utf-8 -*-
"""
MLDIVIDE    Backslash or left matrix divide.

Created on Wed Jul 17 15:25:05 2013

@author: User
"""
import numpy as np
import scipy.linalg as sci
from spotboxpy.opSpot.isspot import isspot

def mldivide(A,B):
    if np.iscomplexobj(A) or np.iscomplexobj(B):
        cflag = True
    else:
        cflag = False
        
    if not isspot(A):
        if np.isscalar(A):
            x = (1.0/A)*B
        else:    
            if np.size(A,0) != B.m:
                raise Exception ('Matrix dimensions must agree.')
                return
                
            if cflag:
                x = np.zeros((np.size(A,1),B.n),dtype=complex)
            else:
                x = np.zeros((np.size(A,1),B.n))
                
            ej = np.zeros((B.n,1))
            for i in range(B.n):
                ej[i] = 1
                bej = np.dot(B,ej)
                if np.size(A,0) == np.size(A,1):
                    y = sci.solve(A,bej)
                    x[:,i] = y[0]
                else:
                    y = sci.lstsq(A,bej)
                    x[:,i] = y[0]
                    
    elif not isspot(B):
        if A.m != np.size(B,0):
            raise Exception ('Matrix dimensions must agree.')
            return
            
        if cflag:
            x = np.zeros((A.n,np.size(B,1)),dtype=complex)
        else:
            x = np.zeros((A.n,np.size(B,1)))
            
        for i in range(np.size(B,1)):
            x[:,i] = A.divide(B[:,i],1)
            
    else:
        x = np.dot(A.pinv(),B)
        
    return x
                