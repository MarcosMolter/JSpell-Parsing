# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:11:36 2016

@author: marcos
"""
import re

dictionary_pattern = dict(
    word = '^(?P<word>[^\/]+)[\/](?P<tag>[^\/]+)[\/]?(?P<afix>[^\/]+)?[\/]$'
    )


class Word:

    def __init__(self,re_search_word):
        self.word = re_search_word.get('word')
        self.tag = re_search_word.get('tag')
        self.affix = re_search_word.get('afix')
       
class Dictionary:
    
    def __init__(self):
        self.words = []

        
    def f_word(self,re_search):
        self.words.append(Word(re_search.groupdict()))

        

class Dictionarykey:
    def __init__(self,function,pattern):
        self.function = function
        self.pattern = dictionary_pattern.get(pattern)

def load_dictionary_dict(aff_file_path):
    dic_file = open(aff_file_path,'r')
    
    dictionary = Dictionary()
    dictionary_keys = [
        Dictionarykey(dictionary.f_word, 'word')
        ]
        
    for line in dic_file:
        for dictionary_key in dictionary_keys:
            re_search = re.search(dictionary_key.pattern,line)
            if re_search is not None:
               dictionary_key.function(re_search)
            
    return dictionary       

      
        
        
        