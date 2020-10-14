# 2020 GRC Machine Learning Hackathon Scripts

This repository contains the scripts used to preprocess the provided data for the 2020 GRC ML Hackathon.

**What do these do?**
Machine learning models require well-formatted and organized inputs. However, most documentation for datasheets and scientific publications are written to be read by humans. These scripts demo one way of converting many human-readable documents into an organized dataset for training a ML model.

These diagrams describe the conversion process:

<kbd><img src="/images/conversion.png" alt="" width="800"/></kbd>
<kbd><img src="/images/process_scripts_1.png" alt="" width="800"/></kbd>
<kbd><img src="/images/process_scripts_2.png" alt="" width="800"/></kbd>

***These scripts rely on Textricator***
Textricator is an open source PDF text extraction tool - See the below install directions on how to get running

Preprequisites:
- Python 3 https://www.python.org/downloads/

Installing python is outside of the scope of these instructions, but there are many guides online for every system configuration one could have. 

One example, if you don't have Admin rights:
https://stackoverflow.com/questions/33876657/how-to-install-python-any-version-in-windows-when-youve-no-admin-priviledges

Explanation of files here:
- Scripts: Current version of datasheet conversion scripts, requiring minimal user input
- Alternative_Scripts: Old version of conversion scripts. Takes a significantly different approach to covnerting files. Tested and working on a subset of dataset.
- Images: Images embedded in the readme.md file

# How to get Running:

**Short Instructions:**

Download & extract a copy of this repo and textricator 

```
robocopy ./Downloads/2020-grc-machine-learning-hackathon-master/2020-grc-machine-learning-hackathon-master/Scripts/ ./Downloads/textricator-9.2.57-bin/textricator-9.2.57/ /s
cd .\Downloads\textricator-9.2.57-bin\textricator-9.2.57\
0_run_all.bat
cd .\data_folder\
dir
```

**If that doesn't make sense, no worries! Follow the directions below:**

## Step 1: Download a copy of Textrictor

It's a bit difficult to get to the textricator zip, so I've provided screenshots of the process.
Go here: https://github.com/measuresforjustice/

<kbd><img src="/images/textricator_directions_1.png" alt="Textricator directions" width="800"/></kbd>
<kbd><img src="/images/textricator_directions_2.png" alt="Textricator directions" width="800"/></kbd>
<kbd><img src="/images/textricator_directions_3.png" alt="Textricator directions" width="800"/></kbd>

- Extract the files

## Step 2: Download this repository
<kbd><img src="/images/download_repo_instructions.png" alt="Repo directions" width="800"/></kbd>

- Extract the files

## Step 3: Copy scripts into textricator
<kbd><img src="/images/copy-files-1.png" alt="Copy Files" width="800"/></kbd>
<kbd><img src="/images/copy-files-2.png" alt="Copy Files" width="800"/></kbd>

## Step 4: Run preprocessing scripts "0_run_all.bat"
<kbd><img src="/images/run-scripts-1.png" alt="Copy Files" width="800"/></kbd>
<kbd><img src="/images/run-scripts-2.png" alt="Copy Files" width="800"/></kbd>

The raw PDF files are converted and combined into one machine-readable CSV file.

**For details on how each step works, open the python scripts (the ____.py files you copied) in a text editor (e.g. notepad, Spyder IDE, nano, etc.)**
