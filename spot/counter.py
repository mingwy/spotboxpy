# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 15:38:42 2013

@author: User
"""

class Counter(object):
    
    def __init__(self):
        self.mode1 = 0
        self.mode2 = 0
    
    def plus1(self,mode):
        if mode == 1:
            self.mode1 = self.mode1 + 1
            return 1
        elif mode == 2:
            self.mode2 = self.mode2 + 1
            return 1
        else:
            raise Exception('Unrecongnized mode.')
            return 0
    