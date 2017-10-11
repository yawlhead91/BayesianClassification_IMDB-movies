#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:39:28 2017

@author: alexkirwan
"""

import parser as p
import calculate as c

def main():
    # Use Parse module to import dataset prepare fetaures and 
    # vocabulary
    ds = p.ParseData("SmallIMDB")
    
    # Use Calc class to retrive term frequency of each class
    calc =  c.Calculate(ds.vocabulary)
    nf = calc.termFrequency(ds.vocabulary, ds.classes["neg"])
    pf = calc.termFrequency(ds.vocabulary, ds.classes["pos"])
    
    # Get term probability multinomial model formula
    np = calc.termProbability(ds.vocabulary, nf)
    pp = calc.termProbability(ds.vocabulary, pf)
    
    
    
    print(np)
    
    
    return 

main()