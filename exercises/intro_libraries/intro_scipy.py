"""
intro_scipy.py

Ejercicios prácticos para resolver problemas numéricos y estadísticos usando SciPy.
─────────────────────────────────────────────────────────────
Requisitos:
    - numpy
    - scipy
─────────────────────────────────────────────────────────────
"""
# Librerías necesarias
import numpy as np
from scipy import linalg, stats, optimize, signal
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_scipy.log")

################################################################################
# NOTE: Revisa la API de SciPy en https://docs.scipy.org/doc//scipy/index.html #
################################################################################

# Función auxiliar para verificar si una variable es None (CORRECCIÓN 1)
def is_none(var):
    return var is None

# Ejercicio 1: Resolver un sistema lineal Ax = b
# 
# TODO: Define A y b como arreglos NumPy y encuentra x. Los valores son: A = [[3, 1], [1, 2]], b = [9, 8]
#
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])  # CORRECCIÓN 2: cambiar la B por b
linear_system = linalg.solve(A, b)

# Impresion de la salida linear_system
plog(f"linear_system: {linear_system}", level=ERROR if is_none(linear_system) else DEBUG, eol=True)

# Ejercicio 2: Calcular determinante y matriz inversa
#
# TODO: Obten el determinante y la inversa de la matriz A del ejercicio anterior
#
determinant = linalg.det(A)
inverse = linalg.inv(A)

# Impresion de la salida determinant e inverse (CORRECCIÓN 3)
plog(f"determinant: {determinant}, inverse:\n{inverse}", 
     level=ERROR if is_none(determinant) or is_none(inverse) else DEBUG, eol=True)

# Ejercicio 3: Estadísticas básicas sobre una muestra
# 
# TODO: Obtén la media, desviación estándar y moda sobre un arreglo de datos [1, 2, 2, 3, 4, 4, 4, 5]
# 
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])  # CORRECCIÓN 4: datos completos
mean = np.mean(data)
tstd = np.std(data)
mode_result = stats.mode(data)  # CORRECCIÓN 5: cambié "mode" por "mode_result"

# Impresion de la salida mean, tstd, mode (CORRECCIÓN 6)
plog(f"media: {mean}, desviación estándar: {tstd}, moda: {mode_result}", 
     level=ERROR if is_none(mean) or is_none(tstd) or is_none(mode_result) else DEBUG, eol=True)

# Ejercicio 4: Ajuste de una función cuadrática
# 
# TODO: Encuentra el mínimo de una función f(x) = (x - 3)^2 + 2
#
def f(x):
    return (x-3)**2 + 2

# CORRECCIÓN 7: Manejo seguro del resultado
result = optimize.minimize(f, x0=0)
f_min = result.x[0] if result.success else None

# Impresion de la salida f_min
plog(f"Mínimo encontrado en x = {f_min}", level=ERROR if is_none(f_min) else DEBUG, eol=True)

# Ejercicio 5: Transformada de Fourier de una señal
#
# TODO: Obten el espectro de una señal compuesta. Señal: sin(2π5t) + sin(2π20t)
#
t = np.linspace(0, 1, 500) # tiempo
signal_5hz = np.sin(2 * np.pi * 5 * t)
signal_20hz = np.sin(2 * np.pi * 20 * t)
composite_signal = signal_5hz + signal_20hz
t_fourier = np.fft.fft(composite_signal)

# Impresion de la salida t_fourier (CORRECCIÓN 8: mostrar solo primeras muestras)
plog(f"F.T. (primeras 5 componentes): {t_fourier[:5]}", level=ERROR if is_none(t_fourier) else DEBUG, eol=True)

# Ejercicio 6: Filtrado de señal con Butterworth
#
# TODO: Usa signal.butter y signal.filtfilt para aplicar un filtro pasa-bajas. Nyquist = 0.5 * fs, low = 10 / Nyquist. Ruido: sin(2π5t) + 0.5sin(2π50t)")
#
fs = 100.0  # frecuencia de muestreo
nyquist = 0.5 * fs
cutoff = 10.0 #Hz
normal_cutoff = cutoff / nyquist

t_filter = np.linspace(0, 1, int(fs))
signal_clean = np.sin(2 * np.pi * 5 * t_filter)
noise = 0.5 * np.sin(2 * np.pi * 50 * t_filter)
noisy_signal = signal_clean + noise

b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)
lp_filter = signal.filtfilt(b, a, noisy_signal)

# Impresion de la salida lp_filter (CORRECCIÓN 9: mostrar solo primeras muestras)
plog(f"Filtro Pasa-Bajas (primeras 5 muestras): {lp_filter[:5]}", level=ERROR if is_none(lp_filter) else DEBUG, eol=True)

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la solución de Ax = b en términos geométricos?
# Es la intersección entre las dos líneas 
# - ¿Por qué es útil conocer la moda y la desviación estándar de una muestra?
# Para conocer su valor más frecuente, conocer la tendencia.
# - ¿Qué información nos da la transformada de Fourier de una señal?
# Nos permite analizar la señal en el dominio de la frecuencia
# - ¿Qué efecto tiene un filtro Butterworth sobre una señal compuesta?
# Atenúa las frecuencias por encima de las frecuencias de corte mientras mantiene las frecuencias bajas.
