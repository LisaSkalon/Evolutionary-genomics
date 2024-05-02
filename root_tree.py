#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:31:18 2023

@author: gospozha
"""

import os
from ete3 import Tree

# set working dir
os.chdir("/home/gospozha/EvoGen/monoph/")
for filename in os.listdir('/home/gospozha/EvoGen/monoph/aln2/'):
    if filename.endswith('.treefile'):
            tree = Tree(os.path.join('/home/gospozha/EvoGen/monoph/aln2/', filename))
            
            tree.set_outgroup("centralis")
            tree.set_outgroup("cricetulus")
            tree.write(format = 3, outfile  = (os.path.join('/home/gospozha/EvoGen/monoph/aln2/root/', filename)))
            

