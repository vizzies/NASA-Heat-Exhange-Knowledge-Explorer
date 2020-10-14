@ECHO OFF 
TITLE Process All Datasheets
ECHO Please wait... Running data preprocessing scripts
:: Script 1: Run textricator. 
ECHO ============================
ECHO Running 1_process_all.py
ECHO ============================
python 1_process_all.py ".\\data_folder\\"
:: Section 2: Extract information.
ECHO ============================
ECHO Running 2_text_reformat.py
ECHO ============================
python 2_text_reformat.py ".\\data_folder\\"
:: Section 3: Combine files.
ECHO ============================
ECHO Running 3_merge_formatted.py
ECHO ============================
python 3_merge_formatted.py ".\\data_folder\\"

PAUSE