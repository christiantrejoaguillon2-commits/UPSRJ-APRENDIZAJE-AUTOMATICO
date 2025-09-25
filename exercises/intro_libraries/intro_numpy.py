"""
 intro_numpy.py

Ejercicios prácticos para manipular arreglos y operaciones numéricas usando NumPy.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - numpy
─────────────────────────────────────────────────────────────

autor: https://github.com/chucholoport
fecha: 11/09/2025
"""
# Librerías necesarias
import numpy as np
import sys
import os
from logging import DEBUG, ERROR

# Ajustar el import path para py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_numpy.log")

#########################################################################
# NOTE: Revisa la API de Numpy en https://numpy.org/doc/1.21/reference/ #
#########################################################################

# Ejercicio 1: Crear un arreglo de 10 ceros
arg1 = np.zeros(10)
plog(f"arreglo 1: {arg1}", level=ERROR if arg1 is None else DEBUG, eol=True)

# Ejercicio 2: Crear un arreglo de números del 10 al 49
arg2 = np.arange(10, 50)
plog(f"arreglo 2: {arg2}", level=ERROR if arg2 is None else DEBUG, eol=True)

# Ejercicio 3: Invertir el arreglo anterior
arg3 = arg2[::-1]
plog(f"arreglo 3: {arg3}", level=ERROR if arg3 is None else DEBUG, eol=True)

# Ejercicio 4: Crear una matriz 3x3 con valores del 0 al 8
mat = np.arange(9).reshape(3, 3)
plog(f"matriz:\n{mat}", level=ERROR if mat is None else DEBUG, eol=True)

# Ejercicio 5: Encontrar índices de elementos mayores a 5
indices = np.argwhere((mat > 5))
plog(f"indices: {indices}", level=ERROR if len(indices) == 0 else DEBUG, eol=True)

# Ejercicio 6: Calcular la media, mediana y desviación estándar
mean = np.mean(arg2)
median = np.median(arg2)
std = np.std(arg2)
plog(f"mean: {mean}, median: {median}, std: {std}", 
     level=ERROR if None in (mean, median, std) else DEBUG, eol=True)

# Ejercicio 7: Crear una matriz identidad de tamaño 4x4
identity = np.eye(4)
plog(f"identity:\n{identity}", level=ERROR if identity is None else DEBUG, eol=True)

# Ejercicio 8: Multiplicar dos matrices compatibles
A = np.arange(1, 5).reshape(2, 2)
B = np.arange(5, 9).reshape(2, 2)
product = np.dot(A, B)
plog(f"A:\n{A}\nB:\n{B}\nproduct:\n{product}", 
     level=ERROR if product is None else DEBUG, eol=True)

# Ejercicio 9: Normalizar un arreglo
def normalize(arr):
    return (arr - arr.min()) / (arr.max() - arr.min())

normalized = normalize(arg2)
plog(f"normalized: {normalized}", level=ERROR if normalized is None else DEBUG, eol=True)

# Ejercicio 10: Arreglo aleatorio y conteo
np.random.seed(0)
random_arr = np.random.rand(100)
count = np.sum(np.logical_and(random_arr >= 0.3, random_arr <= 0.7))
plog(f"count: {count}", level=ERROR if count is None else DEBUG, eol=True)


# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué diferencia hay entre np.array y np.arange?
#   -> np.array crea un arreglo a partir de una lista dada, mientras que np.arange genera secuencias de números en un rango definido.
#
# - ¿Por qué es útil la matriz identidad en álgebra lineal?
#   -> Porque es el elemento neutro en la multiplicación de matrices (A * I = A), y se usa para invertir matrices y resolver sistemas de ecuaciones.
#
# - ¿Qué significa normalizar un arreglo y cuándo se usa?
#   -> Es reescalar valores a un rango estándar (ej. 0–1). Se usa en machine learning y procesamiento de datos para que las variables tengan la misma escala.
