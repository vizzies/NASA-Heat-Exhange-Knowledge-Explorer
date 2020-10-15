from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from pathlib import Path


flattened_string = []
path = input()

for index, fp in enumerate(Path(path).iterdir()):
    output_string = StringIO()
    with open(fp, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    with open("{0}\\Processed PDFs\\{1}.txt".format(path, index), "w", encoding="utf-8") as fd:
        fd.write(output_string.getvalue())

    flattened_string.append(output_string.getvalue().replace("\r", " ").replace("\n", " "))

with open("{0}\\combined_text2.txt".format(path), "w", encoding="utf-8") as fd:
    fd.write("\n".join(flattened_string))