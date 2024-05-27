import pandas as pd
import numpy as np

#carga de base de datos
path1='C:/temporal/Python/read_excel_data/Entorno1/Data.xlsx'
Excel=pd.read_excel(path1,sheet_name='Sheet1')

#obtener el index de la ultima fila
ultima_fila= Excel.index[-1]

n1= 'kdsss'; n2='ababababa';n3= '1111111';n4='dsdsdsds'

Excel.loc[ultima_fila+1,'Modelo'] = n1
Excel.loc[ultima_fila+1,'No_De_Serie'] = n2
Excel.loc[ultima_fila+1,'Clave1'] = n3
Excel.loc[ultima_fila+1,'Clave2'] = n4

#guardar los cambios en el archivo en excel
Excel.to_excel(path1,sheet_name="Sheet1", index=False, header=True)

print(ultima_fila)