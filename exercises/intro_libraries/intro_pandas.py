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
import sys
import os
from logging import DEBUG, ERROR

# Ajustar path para importar py_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_pandas.log")

#########################################################################
# NOTE: Revisa la API de Pandas en https://pandas.pydata.org/docs/      #
#########################################################################

input_csv  = 'exercises/intro_libraries/inputs/estudiantes.csv'
input_json = 'exercises/intro_libraries/inputs/estudiantes.json'
input_yaml = 'exercises/intro_libraries/inputs/estudiantes.yaml'

# Ejercicio 01: Manejo de archivos CSV
input_csv = '../exercises/intro_libraries/inputs/estudiantes.csv'
plog(f"csv: {csv_data}", level=ERROR if csv_data is None else DEBUG, eol=True)

# Ejercicio 02: Manejo de archivos JSON
json_data = pd.read_json(input_json)
plog(f"json: {json_data}", level=ERROR if json_data is None else DEBUG, eol=True)

# Ejercicio 03: Manejo de archivos YAML
with open(input_yaml, "r", encoding="utf-8") as f:
    yaml_loaded = yaml.safe_load(f)
yaml_data = pd.DataFrame(yaml_loaded)
plog(f"yaml: {yaml_data}", level=ERROR if yaml_data is None else DEBUG, eol=True)

# Ejercicio 04: Mostrar el encabezado del DataFrame
df_head = csv_data.head()
plog(f"DataFrame head: {df_head}", level=ERROR if df_head is None else DEBUG, eol=True)

# Ejercicio 05: Filtrado de información (promedio > 9)
above_nine = csv_data[csv_data["promedio"] > 9]
plog(f"Estudiantes con promedio > 9: {above_nine}", level=ERROR if above_nine is None else DEBUG, eol=True)

# Ejercicio 06: Agrupamiento y estadísticas
career_group = csv_data.groupby("carrera")["promedio"].mean()
general_mean = csv_data["promedio"].mean()
plog(f"Promedio por carrera: {career_group}", level=ERROR if career_group is None else DEBUG, eol=True)
plog(f"Promedio general: {general_mean}", level=ERROR if general_mean is None else DEBUG, eol=True)

# Ejercicio 07: Conteo por categoría (género)
total_male = csv_data[csv_data["genero"] == "M"].shape[0]
total_female = csv_data[csv_data["genero"] == "F"].shape[0]
plog(f"Total hombres: {total_male}", level=ERROR if total_male is None else DEBUG, eol=True)
plog(f"Total mujeres: {total_female}", level=ERROR if total_female is None else DEBUG, eol=True)

# Ejercicio 08: Exportar datos
output_dir = "exercises/intro_libraries/outputs"
os.makedirs(output_dir, exist_ok=True)

above_nine.to_csv(os.path.join(output_dir, "excelentes.csv"), index=False)
above_nine.to_json(os.path.join(output_dir, "excelentes.json"), orient="records", indent=4)
with open(os.path.join(output_dir, "excelentes.yaml"), "w", encoding="utf-8") as f:
    yaml.dump(above_nine.to_dict(orient="records"), f, allow_unicode=True)

# Ejercicio 09: Comparar formatos
csv_count = pd.read_csv(os.path.join(output_dir, "excelentes.csv")).shape[0]
json_count = pd.read_json(os.path.join(output_dir, "excelentes.json")).shape[0]
with open(os.path.join(output_dir, "excelentes.yaml"), "r", encoding="utf-8") as f:
    yaml_count = len(yaml.safe_load(f))

count_compare = {"csv": csv_count, "json": json_count, "yaml": yaml_count}
plog(f"Registros en CSV/JSON/YAML: {count_compare}", level=ERROR if count_compare is None else DEBUG, eol=True)
