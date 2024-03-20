import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Supongamos que estos son los voltajes (en voltios) medidos durante la descarga del capacitor
voltajes = [9.0, 5.5, 2.3]  # Ejemplo de voltajes medidos
tiempo_inicial = 0  # El tiempo inicial es 0
tiempo_final = 10  # Ejemplo de tiempo final en segundos

# Estimamos tiempos intermedios suponiendo una distribución equitativa
tiempos = np.linspace(tiempo_inicial, tiempo_final, len(voltajes))


# Definimos la función de descarga de un capacitor
def modelo_descarga(t, Vb, RC):
    return Vb * np.exp(-t / RC)


# Ajustamos el modelo a los datos para encontrar Vb y RC
parametros_optimizados, _ = curve_fit(
    modelo_descarga,
    tiempos,
    voltajes,
    p0=[voltajes[0], (tiempo_final - tiempo_inicial) / 3],
)

Vb_estimado, RC_estimado = parametros_optimizados

# Usamos los parámetros optimizados para generar la curva de descarga
tiempos_modelo = np.linspace(tiempo_inicial, tiempo_final, 100)
voltajes_modelo = modelo_descarga(tiempos_modelo, Vb_estimado, RC_estimado)

# Graficamos los datos y el modelo
plt.scatter(tiempos, voltajes, label="Datos medidos")
plt.plot(tiempos_modelo, voltajes_modelo, label="Modelo de descarga", color="red")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Curva de Descarga del Capacitor")
plt.legend()
plt.show()
