"""
📊 hw_integrated_exercise.py

Ejercicio integrado que combina Pandas, NumPy y SciPy para analizar datos estudiantiles.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - pandas
    - numpy
    - scipy
─────────────────────────────────────────────────────────────
"""
# Librerías necesarias
import pandas as pd
import numpy as np
from scipy import stats, linalg
import logging
import sys
import os

# Solución al error: Crear nuestras propias funciones de logging
def set_logging(log_file="integrated_exercise.log"):
    """Configura el sistema de logging básico"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='w'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def plog(message, level=logging.INFO, eol=True):
    """Función similar a plog usando logging estándar"""
    if not eol:
        message = message.replace('\n', ' ')
    
    if level == logging.DEBUG:
        logging.debug(message)
    elif level == logging.INFO:
        logging.info(message)
    elif level == logging.WARNING:
        logging.warning(message)
    elif level == logging.ERROR:
        logging.error(message)

# Configurar logging
set_logging(log_file="integrated_exercise.log")

# Función auxiliar para verificar None
def is_none(var):
    return var is None

# Paso 1: Cargar datos desde CSV
#
# TODO: Cargar el archivo 'estudiantes.csv' en un DataFrame llamado df
#
# Primero vamos a crear datos de ejemplo si el archivo no existe
if not os.path.exists('estudiantes.csv'):
    # Crear datos de ejemplo
    data = {
        'nombre': ['Ana', 'Luis', 'Maria', 'Carlos', 'Elena', 'Pedro', 'Laura', 'Javier'],
        'edad': [20, 22, 21, 23, 20, 24, 22, 21],
        'carrera': ['Ingeniería', 'Medicina', 'Derecho', 'Ingeniería', 'Arquitectura', 'Medicina', 'Derecho', 'Ingeniería'],
        'cuatrimestre': [5, 7, 6, 8, 4, 9, 5, 6],
        'promedio': [85.5, 92.3, 78.9, 88.7, 95.1, 82.4, 90.6, 87.2]
    }
    df_example = pd.DataFrame(data)
    df_example.to_csv('estudiantes.csv', index=False)
    plog("Archivo 'estudiantes.csv' creado con datos de ejemplo", level=logging.INFO)

df = pd.read_csv('estudiantes.csv')

# Impresion de la salida df
plog(f"DataFrame cargado:\n{df.head()}", level=logging.ERROR if df is None else logging.DEBUG, eol=True)

# Paso 2: Conversión de datos
#
# TODO: Convertir la columna 'promedio' a un arreglo NumPy
#
promedio = df['promedio'].to_numpy()

# Impresion de la salida promedio
plog(f"Promedios como array NumPy: {promedio}", level=logging.ERROR if is_none(promedio) else logging.DEBUG, eol=True)

# Paso 3: Manipulación de datos
# 
# TODO: Normalizar los promedios entre 0 y 1
#
# NOTE: Aplicar la fórmula de normalización: (x - min) / (max - min)
#
min_promedio = np.min(promedio)
max_promedio = np.max(promedio)
normalized = (promedio - min_promedio) / (max_promedio - min_promedio)

# Agregar la columna normalizada al DataFrame
df['promedio_normalizado'] = normalized

# Impresion de la salida normalized
plog(f"Promedios normalizados: {normalized}", level=logging.ERROR if is_none(normalized) else logging.DEBUG, eol=True)

# Paso 4: Calcular estadísticas
#
# TODO: Usar stats.tmean, stats.tstd y stats.mode sobre el arreglo de promedios
#
mean = stats.tmean(promedio)
tstd = stats.tstd(promedio)
mode_result = stats.mode(promedio)

# Impresion de la salida mean, tstd, mode
plog(f"Media recortada: {mean:.2f}, Desviación estándar recortada: {tstd:.2f}, Moda: {mode_result}", 
     level=logging.ERROR if is_none(mean) or is_none(tstd) or is_none(mode_result) else logging.DEBUG, eol=True)

# Paso 5: Filtrar estudiantes con promedio normalizado > 0.8
#
# TODO: Crear un nuevo DataFrame con estudiantes destacados
#
destacados = df[df['promedio_normalizado'] > 0.8]

# Impresion de la salida destacados
plog(f"Estudiantes destacados:\n{destacados}", level=logging.ERROR if is_none(destacados) else logging.DEBUG, eol=True)

# Paso 6: Crear matriz de características para álgebra lineal
# 
# TODO: Usar columnas numéricas como 'edad', 'cuatrimestre' y 'promedio_normalizado'
#
mat = df[['edad', 'cuatrimestre', 'promedio_normalizado']].to_numpy()

# Impresion de la salida mat
plog(f"Matriz de características:\n{mat}", level=logging.ERROR if is_none(mat) else logging.DEBUG, eol=True)

# Paso 6.1: Calculo de matrices
#
# TODO: Calcular la matriz de covarianza
#
covarianza = np.cov(mat, rowvar=False)

# Impresion de la salida covarianza
plog(f"Matriz de covarianza:\n{covarianza}", level=logging.ERROR if is_none(covarianza) else logging.DEBUG, eol=True)

# Paso 6.2: Calculo de matrices
#
# TODO: Calcular la inversa de la matriz
#
if covarianza.shape[0] == covarianza.shape[1]:
    try:
        inversa = linalg.inv(covarianza)
    except linalg.LinAlgError:
        inversa = None
        plog("La matriz de covarianza es singular y no se puede invertir", level=logging.WARNING)
else:
    inversa = None

# Impresion de la salida inversa
plog(f"Inversa de la matriz de covarianza:\n{inversa}", level=logging.ERROR if is_none(inversa) else logging.DEBUG, eol=True)

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la matriz de covarianza en este contexto?
#   Representa como varían conjuntamente las características de los estudiantes. Una covarianza positiva indica que cuando
#   una variable aumenta, la otra tiende a aumentar también.

# - ¿Qué variables parecen estar más relacionadas entre sí?
#   La covarianza entre edad y cuatrimestre es alta, es decir, estudiantes de mayor edad tienden  a estar en cuatrimestres
#   más avanzados.

# - ¿Qué significa que un estudiante tenga promedio normalizado > 0.8?
#   Significa que su promedio se encuentra en el 20% superior de todos los promedios del grupo.

# - ¿Cómo podrías extender este análisis para incluir variables categóricas como carrera o género?
#   Se podría utilizar one-hot encoding para convertir las variables categóricas en 
#      variables numéricas binarias. Por ejemplo, la columna "carrera" se podría transformar
#      en múltiples columnas como "carrera_Ingeniería", "carrera_Medicina", etc.