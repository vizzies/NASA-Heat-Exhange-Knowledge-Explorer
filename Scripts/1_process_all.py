"""
1_process_all.py
Author: Karsten Look (GRC-LTE0)
Updated: 18 Sept 2020

This script runs textricator in text mode on the first file in every subdirectory
"""


import os
import glob
import sys

#Example Run Command: python 1_process_all.py ".\\data_folder\\"

input_path= sys.argv[1]
    
for f in glob.glob(os.path.join(input_path,'*.pdf')): #For all files in the folder: runs textricator, save output to same folder

    csv_name = os.path.join(input_path,os.path.splitext(os.path.basename(f))[0]+"_extracted.csv")
        
    cmd = '.\\textricator.bat text --input-format=pdf.itext5 \"{0}\" \"{1}\"'.format(".\\"+f, ".\\"+csv_name)
    print('Output Command:'+cmd) #Say what you are running
    os.system(cmd) #Then run it

