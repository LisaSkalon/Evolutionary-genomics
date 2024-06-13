#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:35:18 2023

@author: gospozha
"""
# Checking monophyly of the clades with ete3

from ete3 import Tree
import os
import pandas as pd

tax=[]
rad1=[]
rad2=[]
rad3=[]

# Path to the directory; iterating through multiple tree files
os.chdir("/home/gospozha/EvoGen/monoph/")
for filename in os.listdir('/home/gospozha/EvoGen/monoph/aln2/root/'):
    if filename.endswith('.treefile'):
            t = Tree(os.path.join('/home/gospozha/EvoGen/monoph/aln2/', filename))
  #  line = '/home/gospozha/EvoGen/monoph/aln/root/OrthoGroup9.fasta.contree'

            tax.append(filename)
        # Listing the species which we want to check
            rad1.append(t.check_monophyly(values=[ "sibiricus", "schisticolor" ], target_attr="name")[1])
            rad2.append(t.check_monophyly(values=["centralis", "glareolus", "semicanus", 
                                                  "tuvinicus", "rutilus", "rufocanus",
                                                  "macrotis", "lemminus"], target_attr="name")[1])
            rad3.append(t.check_monophyly(values=["fortis","subterraneus","oeconomus",
                                                  "raddei","obscurus",
                                                  "agrestis", "gregalis", "pennsylvanicus",
                                                   "brandtii","mandarinus",
                                                  "ochrogaster"], target_attr="name")[1])
# Creating a dataframe with results and saving it
df = pd.DataFrame(list(zip(tax, rad1, rad2, rad3)),
               columns =['Name', 'rad1', 'rad2', 'rad3'])
df.to_csv("/home/gospozha/EvoGen/monoph/aln2/ete3-4.csv")
