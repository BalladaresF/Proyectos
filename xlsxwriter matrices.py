from unicodedata import decimal
import numpy as num
import xlsxwriter

path = ('D:\Visual Studio code\\Python projects\\Excels\\')

excel = xlsxwriter.Workbook(path+"Matrices.xlsx")
hoja1 = excel.add_worksheet()

#formato de celdas:
cr_format = excel.add_format({
    'bold':True,
    'fg_color':'FACC78',
    'border':1,
    'align': 'center'
})

cell_format = excel.add_format({
    'bold':True,
    'fg_color':'6C83D9',
    'align':'center'
})

sum_format = excel.add_format({
    'fg_color':'84F0C8',
    'align':'center'
})

title_format = excel.add_format({
    'bold':True
})

vp_format = excel.add_format({
    'bold':True,
    'fg_color':'6C83D9',
    'align':'center',
    'border':1
})

vec_format = excel.add_format({
    'fg_color':'B8DA65',
    'align': 'center'
})

comp_format = excel.add_format({
    'fg_color':'FF8583',
    'border': 1,
    'bold': True,
    'align': 'center'
})

num_format = excel.add_format({
    'border': 1,
    'align': 'center'
})

#ingreso de datos y manejo de fórmulas:
size = int(input('ingrese la cantidad de criterios: '))
general = num.identity(size)
cr_list = range(1, size+1)

decimal=3
fila = 1
col = 0

while col < size:
    while fila < size:
        cf = fila + 1
        cc = col + 1
        value = int(input('Criterio '+ str(cf) + ' contra criterio '+ str(cc) + ': '))
        #para identificar fracciones (colocar números negativos, como -5 para 1/5):
        if value>0:
            general[fila, col]=value
            general[col, fila]=round(1/value, decimal)
        else:
            value = abs(value)
            general[fila, col]=round(1/value, decimal)
            general[col, fila]=value
        fila+=1
    col+=1
    fila = col+1

sum1 = num.apply_along_axis(sum, 0, general)
norm = general.copy()
col=0
fila=0

while col<size:
    while fila<size:
        norm[fila, col] = round(norm[fila, col]/sum1[col], decimal)
        fila+=1
    col+=1
    fila=0

sum2 = num.apply_along_axis(sum, 0, norm)
vec = num.apply_along_axis(sum, 1, norm)
vp = vec/size
vp = num.around(vp, decimal)
vp = vp.reshape(size, 1)

comp = num.apply_along_axis(sum, 0, vp)

#mostrar datos en consola:
print(general)
print('\n')
print(norm)
print('\n')
print(vp)
print('\n')
print(comp)
print('\n')

#ingreso de datos al Excel:
hoja1.write_column(1, 0, cr_list, cr_format)
hoja1.write_row(0, 1, cr_list, cr_format)

fila=1
for col, data in enumerate(general):
    hoja1.write_column(fila, col+1, data, num_format)

fila=size+1
hoja1.write(fila, 0, "suma Y", cell_format)

col=1
for data in sum1:
    hoja1.write(fila, col, data, sum_format)
    col+=1

fila = size+3
col=0

hoja1.write(fila, col+1, "Normalizada Y", title_format)
hoja1.write_column(fila+2, col, cr_list, cr_format)
hoja1.write_row(fila+1, col+1, cr_list, cr_format)
hoja1.write(fila+1, size+1, "suma X", cell_format)
hoja1.write(fila+1, size+3, "VP", cell_format)

for col, data in enumerate(norm):
    hoja1.write_column(fila+2, col+1, data, num_format)

for data in vec:
    hoja1.write(fila+2, size+1, data, vec_format)
    fila+=1

fila=size+3
for data in vp:
    hoja1.write(fila+2, size+3, data, vp_format)
    fila+=1

fila = 2*(size+2)+1
hoja1.write(fila, 0, "Suma Y", cell_format)

col=1
for data in sum2:
    hoja1.write(fila, col, data, sum_format)
    col+=1

hoja1.write(fila, size+3, comp, comp_format)

excel.close()