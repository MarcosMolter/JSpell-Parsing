# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 00:00:13 2016

@author: marcos
"""

class Error(Exception):
    """Base class for exceptions in this module."""
    pass 

class NoFilesError(Error):
    """could not find any jspell dictionary files ( .aff , .dic , .irr , .yaml )"""
    pass

class NoResourceError(Error):
    """Could not locate resource"""   
    pass    