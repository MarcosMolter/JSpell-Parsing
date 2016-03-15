# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:22:44 2016

@author: Marcos Molter



"""
# Make version info available
__ver_major__ = 1
__ver_minor__ = 0
__ver_bug__ = 0
__version__ = "%d.%d.%d" % (__ver_major__,__ver_minor__,__ver_bug__)

print 'welcome'

import os
from jspellparsing import utils
from jspellparsing import _jspellparsing

def get_jspell_dir(): 
    jspell_res = utils.get_resource_filename("share\jspell")
    versions = os.listdir(jspell_res)
    lastest_version = max(version for version in versions)
    return "%s\%s" % (jspell_res,lastest_version)
    
def jspell_load_files():  
    jspell_dir = get_jspell_dir()
    jspell = _jspellparsing.jspell(jspell_dir)    
    return jspell
                
jspell = jspell_load_files()             
        
        