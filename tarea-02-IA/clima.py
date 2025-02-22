# Importar librerías necesarias
import pandas as pd
import numpy as np
from google.colab import files

# Leer el archivo CSV

dfCalificaciones = pd.read_csv("calificaciones.csv")

# Mostrar las columnas disponibles en el dataset para verificar nombres
print("\n Nombres de las columnas en el archivo CSV:")
print(dfCalificaciones.columns)

# Asegurar que el nombre de la columna sea el correcto
columna_calif = "Calificación" if "Calificación" in dfCalificaciones.columns else "Calificacion"

# 1. Cargar el dataset y mostrar las primeras filas
print("\n Primeras filas del DataFrame:")
print(dfCalificaciones.head())

# 2. Calcular el promedio de calificaciones por materia
promedioMateria = dfCalificaciones.groupby("Materia")[columna_calif].mean()
print("\n Promedio de calificaciones por materia:")
print(promedioMateria)

# 3. Identificar el estudiante con el promedio más alto 
promedioAlumno = dfCalificaciones.groupby("Estudiante")[columna_calif].mean()
alumnoMejorPromedio = promedioAlumno.idxmax()
mejorPromedio = promedioAlumno.max()

print("\n Estudiante con el mejor promedio:")
print(f"{alumnoMejorPromedio} con un promedio de {mejorPromedio:.2f}")

# 4. Agrupar calificaciones por estudiante y calcular el promedio de cada uno (ya calculado en el paso anterior)
print("\n Promedio de calificaciones por estudiante:")
print(promedioAlumno)

# 5. Identificar cuántos estudiantes tienen un promedio de calificaciones superior a 85 
mejoresAlumnos = (promedioAlumno > 85).sum()
print(f"\n Número de estudiantes con un promedio mayor a 85: {mejoresAlumnos}")

# 6. Encontrar la materia con la mayor cantidad de calificaciones registradas 
materiaConMasCalificaciones = dfCalificaciones["Materia"].value_counts().idxmax()
print(f"\n Materia con más calificaciones registradas: {materiaConMasCalificaciones}")

# 7. Mostrar los 5 estudiantes con el promedio más bajo 
peoresAlumnos = promedioAlumno.nsmallest(5)
print("\n Los 5 estudiantes con el promedio más bajo:")
print(peoresAlumnos)
