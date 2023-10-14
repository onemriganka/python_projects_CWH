import PyPDF2

pdffiles = ["p1.pdf","p2.pdf"]

merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    pdffile = open(filename,"rb")

    pdfReader = PyPDF2.PdfReader(pdffile)
    merger.append(pdfReader)

pdffile.close()

merger.write('merged.pdf')