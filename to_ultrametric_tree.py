#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:49:07 2024

@author: gospozha
"""

import os
from ete3 import Tree

# set working dir
os.chdir("/home/gospozha/EvoGen/astral/")


with open("/home/gospozha/EvoGen/astral/pargenes/astral_run/pargenes.rooted.trees", "r") as file:
    for f in file:
        tree = Tree(f)
        tree.convert_to_ultrametric(tree_length=3)
        with open("pargenes.rooted.trees", "a") as newf:
            newf.write(str(tree.write()) + "\n")
            