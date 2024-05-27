"""
Crear un script donde te deje elegir si quieres ingresar nuevos datos 
bajo el formato del excel visto o como segunda opción si deseas consultar 
contraseñas de una ONT en especifico
"""

import pandas as pd
import numpy as np

#preguntar que opcion elige el usuario
op = input('Elige alguna de las siguientes opciones: (1) Ingresar nuevos datos o (2) Consultar datos existentes')
op = str(op)

#condicional 
if op == '1':
    #carga de base de datos
    path1='Data.xlsx'
    Excel=pd.read_excel(path1,sheet_name='Sheet1')

    #obtener el index dela ultima fila
    ultima_fila= Excel.index[-1]

    n1 = input('Ingresa el modelo: ')
    n2 = input('Ingresa el número de serie: ')
    n3 = input('Ingresa la clave1: ')
    n4 = input('Ingresa la clave2: ')
    #n1= 'kdsss'; n2='ababababa';n3= '1111111';n4='dsdsdsds'

    Excel.loc[ultima_fila+1,'Modelo'] = n1
    Excel.loc[ultima_fila+1,'No_De_Serie'] = n2
    Excel.loc[ultima_fila+1,'Clave1'] = n3
    Excel.loc[ultima_fila+1,'Clave2'] = n4

    #guardar los cambios en el archivo en excel
    Excel.to_excel(path1,sheet_name="Sheet1", index=False, header=True)

    print("los datos agregados fueron: " + n1, n2, n3, n4)

elif op == '2':
    #queremos obtener las claves de una ont en especifico
    #FE3E

    #n= 'ALCLFC2FFE3E'
    ns= input('Ingrese el numero de serie: ')

    x= Excel.index[Excel['No_De_Serie']==ns]
    x= x[0] #para quitar el formato del comando index

    #guardamos las credenciales
    pass1= str(Excel['Clave1'][x])
    pass2= str(Excel['Clave2'][x])

    print("El valor de clave1 es: " + pass1)
    print("El valor de clave2 es: " + pass2)

else:
    print('No es una opción válida')