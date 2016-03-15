# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:03:33 2016

@author: marcos
"""
import os


def get_resource_filename(res):
    
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path,res)
    print path
    if os.path.exists(path):
        return path
    else:
        raise Exception("Could not locate resource '%s'" % (res))
        
        
        