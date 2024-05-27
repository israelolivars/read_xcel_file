import pandas as pd
import numpy as np

#carga de base de datos
path1='Data.xlsx'
Excel=pd.read_excel(path1,sheet_name='Sheet1')

n= 'ababababa' #serial a eliminar
x= Excel.index[Excel['No_De_Serie']==n]
x= x[0]

Excel = Excel.drop(x)

#guardar los cambios en el archivo en excel
Excel.to_excel(path1,sheet_name="Sheet1", index=False, header=True)

print(Excel) #imprime el resto del archivo