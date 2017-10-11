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
    
    # Use Parse module to import dataset prepare fetaures and 
    # vocabulary
    parse = p.ParseData()
    ds = parse.training("SmallIMDB")
    
    # Use Calc class to retrive term frequency of each class
    calc =  c.Calculate(ds[v])
    nf = calc.termFrequency(ds[v], ds[y]["neg"])
    pf = calc.termFrequency(ds[v], ds[y]["pos"])
    
    # Get term probability multinomial model formula
    np = calc.termProbability(ds[v], nf)
    pp = calc.termProbability(ds[v], pf)
    
    
    
    
    return 

main()