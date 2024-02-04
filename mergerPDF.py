import PyPDF2
import os

merger = PyPDF2.PdfMerger(strict=False)

list_files = os.listdir("PDFs")
for file in list_files:
    if ".pdf" in file:
        merger.append(f"PDFs/{file}")

merger.write("mergedFile.pdf")