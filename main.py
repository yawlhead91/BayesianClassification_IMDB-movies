#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:39:28 2017

@author: alexkirwan
"""

import parser as p
import calculate as c

def main():
    # Commonly used data
    
    # Use Parse module to import dataset prepare fetaures and 
    # vocabulary and test data
    parse = p.ParseData()
    sw = parse.stopWords("Stopwords.txt")
    td = parse.test("TestData", sw)
    vocabulary, classcount, documents, classes = parse.training("LargeIMDB", sw)
    
    ln = len(classes["neg"])
    lp = len(classes["pos"])
    
    
    # Make length same on both sets of data
    if  ln > lp:
        classes["neg"] = classes["neg"][0:lp]
    
    if  lp > ln:
        classes["pos"] = classes["pos"][0:ln]
    
    
    # Use Calc class to retrive term frequency of each class
    calc =  c.Calculate(vocabulary)
    nf = calc.termFrequency(vocabulary, classes["neg"])
    pf = calc.termFrequency(vocabulary, classes["pos"])
    
    # Get term probability multinomial model formula
    np = calc.termProbability(vocabulary, nf)
    pp = calc.termProbability(vocabulary, pf)
    
    ncp = calc.classProbability(documents, classcount["neg"])
    pcp = calc.classProbability(documents, classcount["pos"])
    
    negativeResults = []
    postiveResults = []
    correctn = 0
    correctp = 0
    
    # Test all knows negative test documents
    for tst in td["neg"]:
        negativeResults.append(calc.classification(ncp, pcp, np, pp, td["neg"][tst]))
    
        
    # Test all knows negative test documents
    for tst in td["pos"]:
        postiveResults.append(calc.classification(ncp, pcp, np, pp, td["pos"][tst]))
    
    for i in negativeResults:
        if i == False:
            correctn += 1
            
    
    for i in postiveResults:
        if i == True:
            correctp += 1

            
    negp = (correctn/len(td["neg"]))*100
    posp = (correctp/len(td["pos"]))*100
    
    acuracy = (negp+posp)/2
    
    print(acuracy,"% accurate")
    
    return 

main()