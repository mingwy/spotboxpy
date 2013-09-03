# -*- coding: utf-8 -*-
"""
NORMEST    Estimate the matrix 2-norm

Created on Tue Jul 16 15:54:35 2013

@author: User
"""
import numpy as np
import scipy.linalg as sci

def normest(S,tol=1.0e-6,nargout=1):
    maxiter = 100
    m,n = S.size()
    cnt = 0
    
    v = np.ones((m,1))
    v[np.random.randn(m,1) < 0] = -1
    x = np.dot(S.double().conj().T,v)
    x = np.absolute(x)
    
    e = sci.norm(x)
    if e == 0:
        return
    x = x/e
    e0 = 0
    while np.abs(e-e0) > tol*e:
        e0 = e
        Sx = np.dot(S,x)
        if np.sum(Sx!=0) == 0:
            Sx = np.random.rand(Sx.size())
        x = np.dot(S.double().conj().T,Sx)
        normx = sci.norm(x)
        e = normx/sci.norm(Sx)
        x = x/normx
        cnt = cnt + 1
        if cnt > maxiter:
            print 'Warning: SPOT:normest:notconverge\nNORMEST did not converge for %d iterations with tolerance %d' %(maxiter,tol)
            break
    
    if nargout == 1:
        return e
    else:
        return e,cnt     