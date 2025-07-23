import PyPDF2

pdfiles = ["F:/ai/python/projects/1.pdf", "F:/ai/python/projects/2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merger.pdf')