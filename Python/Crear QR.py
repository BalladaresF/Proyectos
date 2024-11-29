# Para crear códigos, inserte el URL y el nombre que desea utilizar.

import pyqrcode 
from pyqrcode import QRCode #para archivos .svg
from PIL import Image #para abrir la imagen
  
# String which represent the QR code 
print("\nInserte el enlace de la página:")
s = input()
  
# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
print("\nInserte el nombre del QR:")
Nombre = input()
path = ('D:\\Visual Studio code\\Python projects\\QRs\\')
url.png(path+Nombre+".png", scale=5, background=[0xFF,0xFF,0xFF]) 

img = Image.open(path+Nombre+".png")
img.show()
