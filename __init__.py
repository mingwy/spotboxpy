# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 12:13:16 2013

@author: User
"""

import os

__dir = os.path.dirname(os.path.realpath(__file__))
for __file in os.listdir(__dir):
    if __file.endswith('.py') and __file != '__init__.py':
        __mod = __file[:-3]
        __class = list(__mod)
        __class[0] = 'O'
        __class = ''.join(__class)
        #__mod = __import__(__mod,globals(),locals(),[__class],-1)
        #exec '%s = getattr(__mod,__class)' %__mod
        exec 'from %s import %s as %s' %(__mod,__class,__mod)


