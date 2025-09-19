"""
intro_pandas.py

Ejercicios prácticos para manipular datos de estudiantes usando Pandas.
─────────────────────────────────────────────────────────────
Requisitos:
    - pandas
    - pyyaml
─────────────────────────────────────────────────────────────
"""
# Librerías necesarias
import pandas as pd
import yaml
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")

#########################################################################
# NOTE: Revisa la API de Pandas en https://pandas.pydata.org/docs/      #
#########################################################################

input_csv  = 'exercises/intro_libraries/inputs/estudiantes.csv'
input_json = 'exercises/intro_libraries/inputs/estudiantes.json'
input_yaml = 'exercises/intro_libraries/inputs/estudiantes.yaml'

# Ejercicio 1: Manejo de archivos CSV
#
# TODO: Cargar el archivo CSV y registrar la cantidad de registros.
#
csv_data = pd.read_csv(input_csv)

# Impresion de la salida csv_data
plog(f"csv: {csv_data}", level=ERROR if csv_data is None else DEBUG, eol=True)

# Ejercicio 02: Manejo de archivos JSON
#
# TODO: Cargar el archivo JSON y registrar la cantidad de registros.
#
json_data = None

# Impresion de la salida json_data
plog(f"json: {json_data}", level=ERROR if json_data is None else DEBUG, eol=True)

# Ejercicio 03: Manejo de archivos YAML
#
# TODO: Cargar el archivo YAML y registrar la cantidad de registros.
#
yaml_data = None

# Impresion de la salida json_data
plog(f"yaml: {yaml_data}", level=ERROR if yaml_data is None else DEBUG, eol=True)

# Ejercicio 04: Mostrar el encabezado del DataFrame
#
# TODO: Mostrar los primeros 5 registros del DataFrame.
#
df_head = None

# Impresion de la salida json_data
plog(f"DataFrame head: {df_head}", level=ERROR if df_head is None else DEBUG, eol=True)

# Ejercicio 05: Filtrado de información
#
# TODO: Filtrar estudiantes con promedio > 9.
#
above_nine = None

# Impresion de la salida above_nine
plog(f"Estudiantes con promedio > 9: {above_nine}", level=ERROR if above_nine is None else DEBUG, eol=True)

# Ejercicio 06: Agrupamiento y estadísticas
#
# TODO: Agrupar por carrera y calcular promedio general.
#
career_group = None
general_mean = None

# Impresion de la salida career_group
plog(f"Promedio por carrera: {career_group}", level=ERROR if career_group is None else DEBUG, eol=True)

# Impresion de la salida general_mean
plog(f"Promedio general: {general_mean}", level=ERROR if general_mean is None else DEBUG, eol=True)

# Ejercicio 07: Conteo por categoría
#
# TODO: Contar estudiantes por género.
#
total_male = None
total_female = None

# Impresion de la salida total_male
plog(f"Total hombres: {total_male}", level=ERROR if total_male is None else DEBUG, eol=True)

# Impresion de la salida total_female
plog(f"Total mujeres: {total_female}", level=ERROR if total_female is None else DEBUG, eol=True)
    
# Ejercicio 08: Exportar datos
#
# TODO: Exportar estudiantes con promedio > 9 (above_nine) a 'outputs/excelentes.csv, 
#       'outputs/excelentes.json' y 'outputs/excelentes.yaml'
#
pass

# Ejercicio 09: Comparar formatos
# 
# TODO: Verificar que los tres formatos tengan el mismo número de registros.
# 
count_compare = None

# Impresion de la salida count_compare
plog(f"Registros en CSV: {count_compare}", level=ERROR if count_compare is None else DEBUG, eol=True)