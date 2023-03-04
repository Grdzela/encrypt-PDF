from pypdf import PdfReader, PdfWriter
from getpass import getpass


pdfwriter = PdfWriter()
pdf = PdfReader('Profile (1).pdf')


for page in pdf.pages:
    pdfwriter.add_page(page)

password = getpass(prompt='Enter Password: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)
