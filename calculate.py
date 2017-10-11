#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:27:23 2017

@author: alexkirwan
"""

class Calculate:
    def __init__(self, v):
        self.vocabulary = v
        return
    
    
    # Get term frequency for given dec of class fetures 
    # @param{ v:vocabulary<set>}
    # @param{ c:classwords<array>}
    def termFrequency(self, v, c):
        rtn = dict.fromkeys(v, 0)
        for w in c:
            if w in rtn:
                rtn[w]+=1
        return rtn
    
    # Calculate probability of each term given 
    # @param{ v:vocabulary<set>}
    # @param{ c:termFreq<dec>}
    def termProbability(self, v, c):
        rtn = dict()
        for t in v:
            rtn[t] = (c[t]+1)/(len(c)+len(v))
        return rtn