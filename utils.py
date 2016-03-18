# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:03:33 2016

@author: marcos
"""
import os
from erros import NoResourceError
from erros import NoFilesError

def get_resource_filename(res):
    
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path,res)
    if os.path.exists(path):
        return path
    else:
        raise NoResourceError("Could not locate resource '%s'" % (res))
        
def get_jspell_dir(): 
    jspell_res = get_resource_filename("share\jspell")
    versions = os.listdir(jspell_res)
    lastest_version = max(version for version in versions)
    return "%s\%s" % (jspell_res,lastest_version)        
        
def load_files():
    files = {}
    jspell_dir = get_jspell_dir()        
    jspell_files = os.listdir(jspell_dir)
    jspell_attr = ['aff','dic','irr','yaml']        
    
    for jspell_file in jspell_files:
        for attr in jspell_attr:                        
            if jspell_file.endswith('.%s' % (attr)):
                files[attr] = os.path.join(jspell_dir,jspell_file)
   
    files_attr = files.keys()
    if not all(map(lambda v: v in files_attr, jspell_attr)):
        raise NoFilesError("could not find any jspell dictionary files ( .aff , .dic , .irr , .yaml )")
   
    return files

        