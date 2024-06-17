from turtle import title
from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series

book = Workbook()
sheet = book.active

#generación de valores:
for i in range(1,15):
    sheet[f'A{i}'] = i

for i in range(1,15):
    sheet[f'B{i}'] = i*10

#creación de la gráfica:
c1 = ScatterChart()
c1.title = 'Gráfico de dispersión.'
c1.style = 13
c1.y_axis.title = 'eje Y'
c1.x_axis.title = 'eje X'

#ingreso de datos a la gráfica:
xvalues = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=14)
yvalues = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=14)
ser=Series(yvalues, xvalues, title='recta')

#guardar gráfica en celda:
c1.series.append(ser)
sheet.add_chart(c1, 'D3')

#guardar Excel:
path = ('C:\\Users\Andres B\\Desktop\Visual Studio code\\Python projects\\Excels\\')
book.save(path+'Prueba_Grafica.xlsx')