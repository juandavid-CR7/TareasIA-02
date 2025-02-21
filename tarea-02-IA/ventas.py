import pandas as pd
import numpy as np

dfVentas = pd.read_csv('ventas.csv')

# Mostrar las primeras filas
print('\n primeras filas del archivo ventas.csv')
print(dfVentas.head())

# 1. Calcular la cantidad total de productos vendidos por categoría 
ventas_por_categoria = dfVentas.groupby("Producto")["Cantidad"].sum()
print('\n Cantidad total de productos vendidos por categoría:')
print(ventas_por_categoria)

# 3. Determinar cuál es el producto con el mayor total de ventas
dfVentas["Total_Venta"] = dfVentas["Cantidad"] * dfVentas["Precio_Unitario"]
productoMayorVentas = dfVentas.groupby("Producto")["Total_Venta"].sum().idxmax()
print('\n El producto con mayor total de ventas es:', productoMayorVentas)

# 4. Encontrar el precio promedio de los productos vendidos
precioPromedio = np.round(dfVentas["Precio_Unitario"].mean(), 2)
print('\n El precio promedio de los productos vendidos es:', precioPromedio)
