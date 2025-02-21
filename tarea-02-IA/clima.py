import pandas as pd
import numpy as np
from google.colab import files

# Leer el archivo CSV

df = pd.read_csv("clima.csv")

# Mostrar las primeras filas del DataFrame para verificar la estructura
print("Primeras filas del DataFrame:")
print(df.head())

# 1. Convertir el dataset en un DataFrame (ya cargado)

# 2. Calcular la temperatura promedio de cada ciudad
tiempoPromedioCiudad = df.groupby("Ciudad")["Temperatura"].mean()

# 3. Determinar el registro con la temperatura más alta y el más bajo en el dataset
registroTiempoMax = df.loc[df["Temperatura"].idxmax()]
registroTiempoMin = df.loc[df["Temperatura"].idxmin()]

# 4. Identificar qué ciudad tuvo la temperatura más alta y cuál la más baja
ciudad_temp_max = registroTiempoMax["Ciudad"]
ciudad_temp_min = registroTiempoMin["Ciudad"]

# 5. Contar cuántos registros tienen una temperatura mayor a 30°C
registros_mayor_30 = df[df["Temperatura"] > 30].shape[0]

# 6. Contar cuántos días en total hay registrados por cada ciudad
dias_por_ciudad = df["Ciudad"].value_counts()

# Mostrar los resultados
print("\nTemperatura promedio por ciudad es :")
print(tiempoPromedioCiudad)

print("\nRegistro con la temperatura más alta:")
print(registroTiempoMax)

print("\nRegistro con la temperatura más baja:")
print(registroTiempoMin)

print(f"\nCiudad con la temperatura más alta: {ciudad_temp_max}")
print(f"Ciudad con la temperatura más baja: {ciudad_temp_min}")

print(f"\nNúmero de registros con temperatura mayor a 30°C: {registros_mayor_30}")

print("\nCantidad de días registrados por cada ciudad:")
print(dias_por_ciudad)
