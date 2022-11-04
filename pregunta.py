"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


import re
import pandas as pd
from datetime import datetime

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    df.dropna(axis = 0, inplace = True)

    for column in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[column] = df[column].str.lower()
        df[column] = df[column].str.replace('_', ' ')
        df[column] = df[column].str.replace('-', ' ')
    

    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)


    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.search("^\d+/", x).group())-1 == 4) else datetime.strptime(x, "%d/%m/%Y"))
    df.drop_duplicates(inplace = True)

    return df
