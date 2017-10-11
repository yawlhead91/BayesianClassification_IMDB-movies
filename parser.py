#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:23:03 2017

@author: alexkirwan
"""
import os
import re

# Pasrse directory and create vocabulary set of uniq words/features
# into a set also save classes fetures into a dictory hold class words inside 
# an array. This save any more reads IO
class ParseData:
    def __init__(self, dirc):
        self.d = dirc
        self.vocabulary = set()
        self.classes = dict()
        
        absPath = os.path.abspath(self.d)
        
        # For each directory in giving path -> for each file in subdir ->
        # read file take unique words
        for d in os.listdir(absPath):
            # If dirctory is not one of a postive or negative class break!
            if d.lower() != "neg" and d.lower() != "pos":
                break
            
            self.classes[d] = []
            
            files = [f for f in os.listdir(os.path.join(absPath, d)) 
            if os.path.isfile(os.path.join(absPath, d, f))]
            
            for f in files:
                of = open(os.path.join(absPath, d, f), "r", encoding="utf8").read().split()
                for word in of:
                    # Strip any special characters, white spaces puntuation ect ..
                    w = re.sub('[^A-Za-z0-9]+','', word)
                    if w:
                        self.classes[d].append(w)
                        self.vocabulary.add(w)
        return
    
    
    
    
                        
    
    