#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:16:14 2023

@author: gospozha
"""
import os
import csv
import pandas as pd
filelocation = "/home/gospozha/EvoGen/rer/genetrees/"
files= [k for k in next(os.walk(f"{filelocation}"))][2]
filenames = []
content=[]
for file in files:
    with open(f"{filelocation}/{file}", 'r') as source_file:
        filenames.append(file.split('.')[0])
        lines = source_file.read()
        content.append(lines.strip('"\n"'))

data = {'Filename':filenames,
        'Content':content}

df = pd.DataFrame(data)
print (df)

df.to_csv(r'/home/gospozha/EvoGen/rer/trees.all.txt', sep='\t', 
          index = False, header=False)