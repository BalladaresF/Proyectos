#para utilizar este código, se debe colocar el pdf en la carpeta de python y colocar el nombre 
#del archivo en la línea 5.

from pdf2docx import Converter

pdf_file = '1. Cap 1. La evolución de los derechos humanos.pdf'
docx_file = '1. Cap 1. La evolución de los derechos humanos.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()