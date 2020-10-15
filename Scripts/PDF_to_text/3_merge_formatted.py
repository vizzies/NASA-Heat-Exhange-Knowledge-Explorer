# -*- coding: utf-8 -*-
"""
3_merge_formatted.py
Created on Fri Aug  7 15:36:21 2020
Author: Karsten Look (GRC-LTE0)
Updated: 18 Sept 2020

This script merges formatted CSV files into one large CSV. Files are concatenated by row, and matching headers are merged
When headers do not match, new columns are added to the merged file and other files missing those columns are left empty

Files to be merged are located by the filename suffix "_newformatted.csv"
"""

import pandas as pd
import re
import glob
import sys

#Example Run Command: python 3_merge_formatted.py ".\\data_folder\\"

runpath = sys.argv[1]
#runpath = '.\\test_output\\' #uncomment to override command line input

print('=== merge_formatted.py === : Processing Files in directory: {}'.format(runpath))

allfiles = glob.glob(runpath+"*_formatted.csv")


formatted = [f for f in allfiles]

print("Found {} formatted files".format(len(formatted)))

for idx, f in enumerate(formatted):
    
    if(not idx):        
        df = pd.read_csv(f, encoding = "ISO-8859-1")
    else:
        df = df.append(pd.read_csv(f,encoding = "ISO-8859-1"))
        

#print(df)
df.to_csv(runpath+'0000_merged.csv',index=False)
print("{} files merged".format(len(formatted)))