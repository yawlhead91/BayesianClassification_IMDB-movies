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
    ds = parse.training("SmallIMDB")
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
    
    # Test all knows negative test documents
    for tst in td["pos"]:
        tpd = calc.classification(ncp, pcp, np, pp, td["pos"][tst])
        print(tpd)
    
    return 

main()