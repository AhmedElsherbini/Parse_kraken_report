#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:50:54 2022

@author: ahmed elsherbini
#the aim of this script to make data 
"""
###########################
import os 
import pandas as pd
import re
import argparse
import numpy as np
import matplotlib.pyplot as plt
import warnings

###########################
warnings.filterwarnings("ignore")
oo = list()
###########################
try:
    for file in os.listdir():
       if file.startswith("k2_report"):
           with open(file) as f:
                 lines = f.readlines()
                 word = "|s__"
                 for line in lines:
                     if word in line:
                        pattern  = ".*" + word
                        line = line[line.index(word) + 1 : ]
                        oo.append((file,line))
    df = pd.DataFrame(oo, columns=['file', "kraken_predicted_spp"])
    df.to_csv('detailed_kraken_taxa.csv', index=False)
    df2 = df.drop_duplicates(subset = "file")
    df2["kraken_predicted_spp"] = df2['kraken_predicted_spp'].str.replace('\d+', '')
    #df2.kraken_predicted_spp = df.kraken_predicted_spp.str.replace('\d+', '')
    df2["kraken_predicted_spp"] = df2['kraken_predicted_spp'].str.replace("s__","")
    df2.to_csv("Best_kraken_taxa.csv",index=False)
    plot = pd.value_counts(df2['kraken_predicted_spp']).plot.bar()
    plot.bar_label(plot.containers[0], label_type='edge',color='red')
    plt.savefig("Kraken_summary.png", bbox_inches='tight')
    plot.margins(y=.1)
    plot 
except:
    print("Something wrong went make sure the files have the right starting k2_report....txt!")      
