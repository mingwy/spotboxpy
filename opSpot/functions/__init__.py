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
        exec 'from %s import %s' %(__mod,__mod)