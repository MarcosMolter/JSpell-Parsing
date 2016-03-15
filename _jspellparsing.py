# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:44:24 2016

@author: marcos
"""

import os,re

class jspell(object):
    
    def __init__(self,jspell_dir):    
        self.files = {}
        self.load_files(jspell_dir)
        
    def load_files(self,jspell_dir):
        jspell_files = os.listdir(jspell_dir)
        jspell_attr = ['aff','dic','irr','yaml']        
        
        for jspell_file in jspell_files:
            for attr in jspell_attr:                        
                if jspell_file.endswith('.%s' % (attr)):
                    self.files[attr] = os.path.join(jspell_dir,jspell_file)
       
        files_attr = self.files.keys()
        if not all(map(lambda v: v in files_attr, jspell_attr)):
            raise Exception("could not find any jspell dictionary files ( .aff , .dic , .irr , .yaml )")
         
    def load_data(self,jtype):
        aff_path = self.files[jtype]
        aff_file = open(aff_path,'r')
        lines = filter(None,map(self.__valid_rule,aff_file))        
        return lines

    def rules_dict(self,rules):
        rules_obj = {}
        bound_obj = [] 
        word_obj = []
        rule_obj = {}
        flag_obj = []
        ps = ['']
        flags = ['']
        def allaffixes(reg):
            rules_obj['allaffixes'] = reg.groupdict()
        def defstringtype(reg):
            rules_obj['defstringtype'] = reg.groupdict()
        def boundarychars(reg):
            bound_obj.append(reg.groupdict()) 
        def wordchars(reg):
            word_obj.append(reg.groupdict())
        def prefixes(reg):
            ps[0] = 'p'
        def suffixes(reg):
            ps[0] = 's'
        def flag(reg):
            groupdict = reg.groupdict()
            flags[0] = groupdict['flag']
            rule_obj[flags[0]] = []
            flag_obj.append(reg.groupdict())
        def rule(reg):
            groupdict = reg.groupdict()
            groupdict['ps'] = ps[0]
            rule_obj[flags[0]].append(groupdict)
           
          
        
        rules_key = [
            dict(
                 function = allaffixes, 
                 pattern = 'allaffixes\s*(?P<turn>\S*)'
            ),
            dict(
                 function = defstringtype, 
                 pattern = 'defstringtype\s?(?P<def>".*")'
            ),
            dict(
                 function = boundarychars, 
                 pattern = 'boundarychars\s*(?P<char>\S*)'
            ),
            dict(
                 function = wordchars, 
                 pattern = 'wordchars\s*(?P<replace>\S*)\s*(?P<replaced>\S*)'
            ),
            dict(
                 function = prefixes, 
                 pattern = 'prefixes'
            ),
            dict(
                 function = suffixes, 
                 pattern = 'suffixes'
            ),
            dict(
                 function = flag, 
                 pattern = 'flag\s+[\+\*](?P<flag>\S):(\s+;\s+"((?P<grama>\S*))")?'
            ),
            dict(
                 function = rule, 
                 pattern = '(?P<regex>.*)\s+>\s+(-(?P<replace>\S*),)?(?P<replaced>\S*)\s+;\s+"(?P<grama>.*)?"'
            )  
        ]        
        
        for rule in rules:
            for rk in rules_key:
                reg = re.search(rk['pattern'],rule)
                if reg is not None:
                    rk['function'](reg)
            
        rules_obj['boundarychars']  = bound_obj
        rules_obj['wordchars'] = word_obj
        rules_obj['flag'] = flag_obj
        rules_obj['rule'] = rule_obj         
            
        return rules_obj

    def jspell_dict(self,js_dict):
        word_obj = [] 
        def word(reg):
            word_obj.append(reg.groupdict()) 
        dict_key = [
            dict(
                 function = word, 
                 pattern = '^(?P<a>[^\/]+)[\/](?P<b>[^\/]+)[\/]?(?P<rule>[^\/]+)?[\/]$'
            )
            ]
        for w in js_dict:
            for dk in dict_key:
                reg = re.search(dk['pattern'],w)
                if reg is not None:
                    dk['function'](reg)
                    
        return word_obj            


    def __valid_rule(self, line):
        line = re.sub(r'\n|#.*','',line)       
        line = line.strip()
        if bool(line):        
            return line
    
    
 #flag\s+[\+\*](?P<flag>\S):(\s+;\s+"((?P<grama>\S*))")?
 #(?P<regex>.*)\s+>\s+(-(?P<replace>\S*),)?(?P<replaced>\S*)\s+;\s+"(?P<grama>.*)?"      
 #allaffixes\s*(?P<turn>\S*)
 #boundarychars\s*(?P<char>\S*)
 #wordchars\s*(?P<replace>\S*)\s*(?P<replaced>\S*)
 #defstringtype\s?(?P<def>".*")
 #suffixes
 #prefixes   
  
    def prt(self):
        print self.files
        
        
        