#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:23:03 2017

@author: alexkirwan
"""
import os
import re
import nltk
from nltk.stem.porter import PorterStemmer


class ParseData:
    
    def __init__(self):
        self.porter_stemmer = PorterStemmer()
        return
   
    
    def stopWords(self, dirc):
        s = set()
        absPath = os.path.abspath(dirc)
        of = open(absPath, "r", encoding="utf8").read()
        allwords = nltk.word_tokenize(of)
        for word in allwords:
            # Strip any special characters, white spaces puntuation ect ..
            w = re.sub('[^A-Za-z0-9]+','', word).lower()
            if w:
                s.add(w)
        
        return s
    
    
    # Pasrse directory and create vocabulary set of uniq words/features
    # into a set also save classes fetures into a dictory hold class words inside 
    # an array. This save any more reads IO
    def training(self, dirc, sw):
        vocabulary = list()
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
                of = open(os.path.join(absPath, d, f), "r", encoding="utf8").read()
                allwords = nltk.word_tokenize(of)
                
                for word in allwords:
                    # Strip any special characters, white spaces puntuation ect ..
                    w = re.sub('[^A-Za-z0-9]+','', word).lower()
                    
                    if w:
                        vocabulary.append(w)
                        classes[d].append(w)
        
            # Implenent n-gram model convert to list to utalize list functionality
            vocabulary = list(zip(vocabulary, vocabulary[1:]))
            classes[d] = list(zip(classes[d], classes[d][1:]))
                        
        return vocabulary, classcount, documents, classes
    
    
    
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
                
                #allwords = nltk.word_tokenize(of)
                #print(allwords)
                for word in of:
                    # Strip any special characters, white spaces puntuation ect ..
                    w = re.sub('[^A-Za-z0-9]+','', word).lower()
                    
                    if w:
                        rtn[d][f].append(w)
                
                rtn[d][f] = list(zip(rtn[d][f], rtn[d][f][1:]))
                
        return rtn
    
    
    
    
    
    
    
    
                        
    
    