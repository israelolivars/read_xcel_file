import pandas as pd
import numpy as np

#carga de base de datos
path1='C:/temporal/Python/read_excel_data/Entorno1/Data.xlsx'
Excel=pd.read_excel(path1,sheet_name='Sheet1')

print(Excel)