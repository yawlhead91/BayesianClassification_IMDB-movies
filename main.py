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
    v = "vocabulary"
    y = "classes"
    d = "documents"
    cc = "classcount"
    
    # Use Parse module to import dataset prepare fetaures and 
    # vocabulary and test data
    parse = p.ParseData()
    ds = parse.training("LargeIMDB")
    td = parse.test("TestData")
    
    # Use Calc class to retrive term frequency of each class
    calc =  c.Calculate(ds[v])
    nf = calc.termFrequency(ds[v], ds[y]["neg"])
    pf = calc.termFrequency(ds[v], ds[y]["pos"])
    
    # Get term probability multinomial model formula
    np = calc.termProbability(ds[v], nf)
    pp = calc.termProbability(ds[v], pf)
    
    ncp = calc.classProbability(ds[d], ds[cc]["neg"])
    pcp = calc.classProbability(ds[d], ds[cc]["pos"])
    
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