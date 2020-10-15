import unicodedata
import os.path

import camelot

def clean(s):
    '''
    Clean up things like ligatures

    Parameters
    ----------
    s : str
        Input string

    Returns
    -------
    cleaned_s: str
        Cleaned up string
    '''
    return unicodedata.normalize("NFKD", s)

pdfs_dir = "/Users/hschilli/Documents/Big Data/GRC AIML Hackathon 2020/vizzies_challenge_a/RawPDFs/"
pdf_file_name = "page3_paper 107_1-s2.0-S0360544215014395-main.pdf"
pdf_file_path = os.path.join(pdfs_dir, pdf_file_name)

# Extract table information
tables = camelot.read_pdf(pdf_file_path,flavor='stream',table_regions=['320,180,600,0'])

# Clean up text in table cells
tables[0].df = tables[0].df.applymap(clean)

# How many tables were found?
print(len(tables))

# Convert table into an HTML page for viewing of the table results
tables[0].df.to_html("table.html")

# See how well Camelot thinks it did
print(tables[0].parsing_report)

# Plot where Camelot thinks text is on the page
camelot.plot(tables[0], kind='text').show()
