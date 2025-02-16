import PyPDF2

with open('./data/dummy.pdf', 'rb',) as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    


with open('./data/dummy.pdf', 'rb',) as file2:
    reader = PyPDF2.PdfReader(file2)
    page = reader.getPage(0)
    print(page.rotateCounterClockwise(90))