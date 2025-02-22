import pandas as pd
import numpy as np


# Leer el archivo CSV

dfCalificaciones = pd.read_csv("calificaciones.csv")

#1 Cargue el dataset y muestre las primeras filas
print("Primeras filas del DataFrame:")
print(dfCalificaciones.head())

# 2. calcule el promedio de calificaciones por materia
promedioMateria = dfCalificaciones.groupby("Materia")["Calificacion"].mean()

# 3. Identifique el estudiante con el promedio mas alto 
promedioAlumno=dfCalificaciones.groupby("Estudiante")["Calificacion"].mean()
alumnoMejorPromedio=promedioAlumno.idxmax()
mejorPromedio=promedioAlumno.max()

#4 Agrupar calificaciones por Estudiante y calcular y calcular el promedio de cada uno
Estudiantes = dfCalificaciones.groupby("Estudiante")["Calificacion"].mean()

# 5. Indentificar cuantos estudiantes tienen un promedio de calificaciones superior a 85 
mejoresAlumnos=(promedioAlumno>85).sum()

# 6 Encuentre la materia con la mayor cantidad de calificaciones registradas 
materiaConMasCalificaciones=dfCalificaciones["Materia"].value_counts().idxmax()

# 7. Muestre los 5 estudiantes con el promedio mas bajo 
peoresAlumnos=promedioAlumno.nsmallest(5)

#imprimir resultados de los incisos

print("\nPromedio de calificaciones por materia:")
print(promedioMateria)

print("\nEstudiante con el mejor promedio:")
print(alumnoMejorPromedio)

print(f"\nNúmero de estudiantes con un promedio mayor a 85: {mejoresAlumnos}")

print(f"\nMateria con más calificaciones registradas: {materiaConMasCalificaciones}")

print("\nLos 5 estudiantes con el promedio más bajo:")
print(peoresAlumnos)




