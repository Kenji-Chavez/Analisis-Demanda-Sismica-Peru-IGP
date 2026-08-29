import pandas as pd
import numpy as np

# 1. Cargar archivo original
ruta_archivo = r'C:\Users\Kenji\Desktop\PROYECTO ANALISIS DE DATOS\IGP_ACELDAT_Peru_2019-2025_Dataset_0.csv'
df = pd.read_csv(ruta_archivo, sep=';', encoding='latin-1')

# 2. Limpieza de nombres de columnas
df.columns = df.columns.str.replace('-', '_')

# 3. Calcular Aceleración Máxima Resultante (PGA)
df['PGA_RESULTANTE'] = np.sqrt(
    df['ACEL_MAX_VERTICAL']**2 + 
    df['ACEL_MAX_NORTE_SUR']**2 + 
    df['ACEL_MAX_ESTE_OESTE']**2
)

# 4. PARSEO DE FECHA Y HORA 
fecha_evento_clean = pd.to_datetime(
    df['FECHA_EVENTO'].astype(str).str.split('.').str[0].str.strip(), 
    format='%Y%m%d', 
    errors='coerce'
)

fecha_corte_clean = pd.to_datetime(
    df['FECHA_CORTE'].astype(str).str.split('.').str[0].str.strip(), 
    format='%Y%m%d', 
    errors='coerce'
)

fecha_final = fecha_evento_clean.fillna(fecha_corte_clean)

hora_clean = (
    pd.to_numeric(df['HORA_EVENTO'], errors='coerce')
    .fillna(0)
    .astype(int)
    .astype(str)
    .str.zfill(6)
)

hora_td = pd.to_timedelta(
    hora_clean.str[:2] + 'h ' + 
    hora_clean.str[2:4] + 'm ' + 
    hora_clean.str[4:] + 's', 
    errors='coerce'
).fillna(pd.Timedelta(seconds=0))

df['FECHA_HORA'] = fecha_final + hora_td
df['ANIO'] = df['FECHA_HORA'].dt.year
df['MES'] = df['FECHA_HORA'].dt.month
df['MES_NOMBRE'] = df['FECHA_HORA'].dt.strftime('%B')

# 5. Formatear UBIGEO a 6 dígitos
df['UBIGEO'] = df['UBIGEO'].astype(str).str.zfill(6)

# 6. SELECCIONAR SOLO LAS COLUMNAS UTILES 
columnas_deseadas = [
    'FECHA_CORTE', 'UBIGEO', 'DEPARTAMENTO', 'PROVINCIA', 'DISTRITO',
    'FECHA_HORA', 'ANIO', 'MES', 'MES_NOMBRE', 'COD_ESTACION',
    'LAT_ESTACION', 'LON_ESTACION', 'ACEL_MAX_VERTICAL',
    'ACEL_MAX_NORTE_SUR', 'ACEL_MAX_ESTE_OESTE', 'PGA_RESULTANTE'
]

df_final = df[columnas_deseadas]

# 7. Guardar el dataset procesado
ruta_salida = r'C:\Users\Kenji\Desktop\PROYECTO ANALISIS DE DATOS\ACELDAT_Peru_Procesado.csv'
df_final.to_csv(ruta_salida, index=False, sep=';', encoding='utf-8-sig')

print("¡Dataset exportado limpiamente para Power BI sin columnas con error!")
print(df_final)