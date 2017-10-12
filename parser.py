#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:23:03 2017

@author: alexkirwan
"""
import os
import re


class ParseData:
    
    def __init__(self):
       return
   
    
    def stopWords(self, dirc):
        s = set()
        absPath = os.path.abspath(dirc)
        of = open(absPath, "r", encoding="utf8").read().split()
        for word in of:
            # Strip any special characters, white spaces puntuation ect ..
            w = re.sub('[^A-Za-z0-9]+','', word).lower()
            if w:
                s.add(w)
        
        return s
    
    
    # Pasrse directory and create vocabulary set of uniq words/features
    # into a set also save classes fetures into a dictory hold class words inside 
    # an array. This save any more reads IO
    def training(self, dirc, sw):
        rtn = dict()
        vocabulary = set()
        classes = dict()
        classcount = dict()
        documents = 0
        
        absPath = os.path.abspath(dirc)
        
        # For each directory in giving path -> for each file in subdir ->
        # read file take unique words
        for d in os.listdir(absPath):
            # If dirctory is not one of a postive or negative class break!
            if d.lower() != "neg" and d.lower() != "pos":
                continue
            
            classes[d] = []
            classcount[d] = 0
            
            files = [f for f in os.listdir(os.path.join(absPath, d)) 
            if os.path.isfile(os.path.join(absPath, d, f))]
            
            for f in files:
                documents += 1
                classcount[d] += 1
                of = open(os.path.join(absPath, d, f), "r", encoding="utf8").read().split()
                for word in of:
                    # Strip any special characters, white spaces puntuation ect ..
                    w = re.sub('[^A-Za-z0-9]+','', word).lower()
                    if w in sw:
                        continue
                    
                    if w:
                        vocabulary.add(w)
                        classes[d].append(w)
                        
        # Append to return dict
        rtn["vocabulary"] = vocabulary
        rtn["classcount"] = classcount
        rtn["documents"] = documents
        rtn["classes"] = classes
        return rtn
    
    
    
    def test(self, dirc, sw):
        
        rtn = dict()
        
        
        absPath = os.path.abspath(dirc)
        
        # For each directory in giving path -> for each file in subdir ->
        # read file take unique words
        for d in os.listdir(absPath):
            # If dirctory is not one of a postive or negative class break!
            
            if d.lower() != "neg" and d.lower() != "pos":
                continue
            
            rtn[d] = dict()
            
            files = [f for f in os.listdir(os.path.join(absPath, d)) 
            if os.path.isfile(os.path.join(absPath, d, f))]
            
            for f in files:
                rtn[d][f] = []
                of = open(os.path.join(absPath, d, f), "r", encoding="utf8").read().split()
                for word in of:
                    # Strip any special characters, white spaces puntuation ect ..
                    w = re.sub('[^A-Za-z0-9]+','', word).lower()
                    if w:
                        rtn[d][f].append(w)
                        
        return rtn
    
    
    
    
    
    
    
    
                        
    
    