# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:11:36 2016

@author: marcos
"""
import re

affixes_pattern = dict(
    affix = '(?P<regex>.*)\s+>\s+(-(?P<displace>\S*),)?(?P<replace>\S*)\s+;\s+"(?P<tag>.*)?"',
    flag = 'flag\s+[\+\*](?P<flag>\S):(\s+;\s+"((?P<tag>\S*))")?',
    suffixes = 'suffixes',
    prefixes = 'prefixes',
    wordchars = 'wordchars\s*(?P<displace>\S*)\s*(?P<replace>\S*)',
    boundarychars = 'boundarychars\s*(?P<char>\S*)',
    defstringtype = 'defstringtype\s?(?P<def>".*")',
    allaffixes = 'allaffixes\s*(?P<turn>\S*)'
    )


class Affix:

    def __init__(self,re_search_affix):
        self.regex = re_search_affix.get('regex').replace(' ','')
        self.pattern = None        
        self.replace_str = None        
        self.replace = re_search_affix.get('replace').replace('\\','')
        self.displace = re_search_affix.get('displace')
        self.tag = re_search_affix.get('tag') 
       
class Flag:

    def __init__(self,re_search_fag):
        self.flag = re_search_fag.get('flag')
        self.tag = re_search_fag.get('tag')
        
class Boundarychars:

    def __init__(self,re_search_boundarychars):
        self.char = re_search_boundarychars.get('char')
        
class Wordchars:

    def __init__(self,re_search_wordchars):
        self.displace = re_search_wordchars.get('displace')
        self.replace = re_search_wordchars.get('replace')
        
class Affixes:
    
    def __init__(self):
        self.affix = {}
        self.flags = []
        self.pattern = None
        self.replace_str = None
        self.wordchars = []
        self.boundarychars = []
        self.defstringtype = None
        self.allaffixes = None
        self.flag = None
        
    def f_allaffixes(self,re_search):
       self.allaffixes = re_search.groupdict()
    
    def f_defstringtype(self,re_search):
        self.defstringtype = re_search.groupdict()

    def f_boundarychars(self,re_search):
        self.boundarychars.append(Boundarychars(re_search.groupdict())) 

    def f_wordchars(self,re_search):
        self.wordchars.append(Wordchars(re_search.groupdict()))

    def f_prefixes(self,re_search):
        self.pattern = r'^%s'
        self.replace_str = '{1}{0}'

    def f_suffixes(self,re_search):
        self.pattern = r'%s$'
        self.replace_str = '{0}{1}'        
        
    def f_flag(self,re_search):
        groupdict = re_search.groupdict()
        self.flag = groupdict['flag']
        self.affix[self.flag] = []
        self.flags.append(Flag(re_search.groupdict()))

    def f_affix(self,re_search):
        new_affix = Affix(re_search.groupdict())            
        new_affix.pattern = self.pattern
        new_affix.replace_str = self.replace_str        
        self.affix[self.flag].append(new_affix)            
        

class Affixkey:
    def __init__(self,function,pattern):
        self.function = function
        self.pattern = affixes_pattern.get(pattern)

def load_affix_dict(aff_file_path):
    aff_file = open(aff_file_path,'r')
    aff_lines = filter(None,map(__valid_line,aff_file))
    
    affixes = Affixes()
    affix_keys = [
        Affixkey(affixes.f_affix, 'affix'),
        Affixkey(affixes.f_flag, 'flag'),
        Affixkey(affixes.f_prefixes, 'prefixes'),
        Affixkey(affixes.f_suffixes, 'suffixes'),
        Affixkey(affixes.f_wordchars, 'wordchars'),
        Affixkey(affixes.f_boundarychars, 'boundarychars'),
        Affixkey(affixes.f_defstringtype, 'defstringtype'),
        Affixkey(affixes.f_allaffixes, 'allaffixes')
        ]
        
    for line in aff_lines:
        for affix_key in affix_keys:
            re_search = re.search(affix_key.pattern,line)
            if re_search is not None:
               affix_key.function(re_search)
            
    return affixes       

def __valid_line(line):
    line = re.sub(r'\n|#.*','',line)       
    line = line.strip()
    if bool(line):        
        return line
      
        
        
        