# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:44:24 2016

@author: marcos
"""

import re
import affixes
import dictionary
import utils

class jspell(object):
    
    def __init__(self):    
        self.files = utils.load_files()
        self.affixes = affixes.load_affix_dict(self.files.get('aff'))
        self.dictionary = dictionary.load_dictionary_dict(self.files.get('dic'))
        self.inflex = self.inflections()
    
    def inflections(self):
        inflection = {}        
        for dictword in self.dictionary.words:
            if dictword.irregular:
                if dictword.word_irr not in inflection.keys():
                   inflection[dictword.word_irr] = [] 
                inflection[dictword.word_irr].append(dictword.word.decode('utf8').lower())
            else:
                inflection[dictword.word] = []
                if dictword.affix is not None:
                    for word_affix in dictword.affix:
                        flag_affix = self.affixes.affix[word_affix]
                        for affix in flag_affix: 
                            reg = re.search(affix.pattern % (affix.regex),dictword.word.upper())
                            if reg is not None:
                                if affix.displace is not None:
                                    p = re.sub(affix.pattern % (affix.displace),affix.replace,dictword.word.upper())
                                else:
                                    p = affix.replace_str.format(dictword.word,affix.replace)
                                inflection[dictword.word].append(p.decode('utf8').lower())                      

        return inflection
    
    def lemmatize(self,w):
        lex = self.inflex       
        find = [k for (k,v) in lex.iteritems() if w.decode('utf8') in v]
        if find == []:
            return w
        else:
            return find[0]
            

        