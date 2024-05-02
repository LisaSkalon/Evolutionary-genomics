#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:52:35 2023

@author: gospozha
"""
import os
import pandas as pd

# set working dir
os.chdir("/home/gospozha/EvoGen/ete3")

# introduce lists
ort = []
lrt1 = []
lrt2 = []
lrt3 = []

ort1 = []
bfree_back = []
bfree_1 = []
bneut_back = []
bneut_1 = []
fb = []

# open ete3 evol files
for filename in os.scandir('rad1-m'):
    if filename.is_file():
        fp = open(filename, 'r')
        # read file line by line and write to the list
        lines = fp.readlines()
        # iterate through lines
        for i, line in enumerate(lines):
            # if line contains a certain string, append lists by lines next to it
            # append lists with lrt p-value info
            if 'LRT' in line:
                    lrt1.append(lines[i+4].split('|')[2].strip())
                    ort.append(fp.name.split('/')[1].split('.')[0])
            # append lists with models info
            if 'SUMMARY BY MODEL' in line:
                if lines[i+10].find('#1') != -1:
                    bfree_1.append(lines[i+10].split('=>')[1].strip())
                    bfree_back.append(lines[i+11].split('=>')[1].strip())
                else:
                    bfree_back.append(lines[i+10].split('=>')[1].strip())
                    bfree_1.append(lines[i+11].split('=>')[1].strip())
              
                
# create tuples from lists and save to tables                
LRT = list(zip(ort,lrt1))
dfLRT = pd.DataFrame(LRT, columns=['ort','M0.vs.b_free'])

dfLRT.to_csv('rad1-mLRT.csv', sep=',',  index=False)

bfree = list(zip(ort, bfree_1, bfree_back))
dfbfree = pd.DataFrame(bfree, columns=['ort','1.omega', 'background.omega'])
dfbfree.to_csv('rad1bfree-m.csv', sep=',',  index=False)
