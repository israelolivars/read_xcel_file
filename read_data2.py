import pandas as pd
import numpy as np

#carga de base de datos
path1='C:/temporal/Python/read_excel_data/Entorno1/Data.xlsx'
Excel=pd.read_excel(path1,sheet_name='Sheet1')

#queremos obtener las claves de una ont en especifico

n= input('Ingrese el numero de serie: ')

x= Excel.index[Excel['No_De_Serie']==n]
x= x[0] #para quitar el formato del comando index

#guardamos las credenciales
pass1= str(Excel['Clave1'][x])
pass2= str(Excel['Clave2'][x])

print(pass1)
print(pass2)