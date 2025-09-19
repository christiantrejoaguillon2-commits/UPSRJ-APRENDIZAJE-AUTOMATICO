"""
📊 intro_numpy.py

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
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_numpy.log")

#########################################################################
# NOTE: Revisa la API de Numpy en https://numpy.org/doc/1.21/reference/ #
#########################################################################

# Ejercicio 1: Crear un arreglo de 10 ceros
#
# TODO: Crea un arreglo 'arg1' de 10 elementos con valor 0. 
#
arg1 = np.zeros(10)

# Impresion de la salida arg1
plog(f"arreglo 1: {arg1}", level=ERROR if arg1 is None else DEBUG, eol=True)

# Ejercicio 2: Crear un arreglo de números del 10 al 49
#
# TODO: Genera los números del 10 al 49 en un arreglo 'arg2'. 
#
arg2 = None

# Impresion de la salida arg2
plog(f"arreglo 2: {arg2}", level=ERROR if arg2 is None else DEBUG, eol=True)

# Ejercicio 3: Invertir el arreglo anterior
#
# TODO: Invierte el orden del arreglo 'arg2', guardando el resultado en 'arg3'. 
#
arg3 = None

# Impresion de la salida arg3
plog(f"arreglo 3: {arg3}", level=ERROR if arg3 is None else DEBUG, eol=True)

# Ejercicio 4: Crear una matriz 3x3 con valores del 0 al 8
#
# TODO: Crea una matriz 3x3 llamada 'mat' con valores del 0 al 8
#
mat = None

# Impresion de la salida mat
plog(f"matriz:\n{mat}", level=ERROR if mat is None else DEBUG, eol=True)

# Ejercicio 5: Encontrar índices de elementos mayores a 5
#
# TODO: Encuentra posiciones donde el valor > 5 en 'mat', guardando los índices en 'indices'
#
indices = None

# Impresion de la salida indices
plog(f"indices: {indices}", level=ERROR if indices is None else DEBUG, eol=True)

# Ejercicio 6: Calcular la media, mediana y desviación estándar
#
# TODO: Calcula la media, mediana y desviaciación estándar sobre el arreglo 'arg2', guardando los resultados en 'mean', 'median' y 'std'
#
mean = None
median = None
std = None

# Impresion de la salida mean, median y std
plog(f"mean: {mean}, median: {median}, std: {std}", level=ERROR if None in (mean, median, std) else DEBUG, eol=True)

# Ejercicio 7: Crear una matriz identidad de tamaño 4x4
#
# TODO: Genera la matriz identidad 4x4 llamada 'identity'
#
identity = None

# Impresion de la salida identity
plog(f"identity:\n{identity}", level=ERROR if identity is None else DEBUG, eol=True)

# Ejercicio 8: Multiplicar dos matrices compatibles
#
# TODO: Crea dos matrices 2x2 llamadas 'A' y 'B', llénalas con numeros sucesivos del 1 al 8, 
#       multiplícalas y guarda el resultado en 'product'
#
A = None
B = None
product = None

# Impresion de la salida product
plog(f"product:\n{product}", level=ERROR if product is None else DEBUG, eol=True)

# Ejercicio 9: Normalizar un arreglo (valores entre 0 y 1)
#
# TODO: Declara una función 'normalize 'que normalice un arreglo usando la fórmula: (x - min) / (max - min), 
#       llamala sobre el arreglo 'arg2' y guarda el resultado en 'normalized'
#
normalized = None

# Impresion de la salida normalized
plog(f"normalized: {normalized}", level=ERROR if normalized is None else DEBUG, eol=True)

# Ejercicio 10: Crear un arreglo aleatorio de 100 elementos y contar cuántos están entre 0.3 y 0.7
#
# TODO: Genera un arreglo 1x100 de numeros aleatorios con una semilla de 0. 
#       Cuenta cuántos valores están entre 0.3 y 0.7 usando np.logical_and, guardando el conteo en 'count'
#
count = None

# Impresion de la salida count
plog(f"count: {count}", level=ERROR if count is None else DEBUG, eol=True)

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué diferencia hay entre np.array y np.arange?
# - ¿Por qué es útil la matriz identidad en álgebra lineal?
# - ¿Qué significa normalizar un arreglo y cuándo se usa?
