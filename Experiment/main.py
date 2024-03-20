import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Supongamos que estos son los voltajes (en voltios) medidos en diferentes tiempos (en segundos)
# durante la descarga del capacitor. El primer valor corresponde al tiempo t=0.
voltajes = [9.0, 5.5, 2.3]  # Ejemplo de voltajes medidos
tiempos = [0, 5, 10]  # Ejemplo de tiempos en los que se midieron los voltajes

# Definimos la función de descarga de un capacitor
def modelo_descarga(t, Vb, RC):
    return Vb * np.exp(-t / RC)

# Ajustamos el modelo a los datos para encontrar Vb y RC
parametros_optimizados, _ = curve_fit(modelo_descarga, tiempos, voltajes)

Vb_estimado, RC_estimado = parametros_optimizados

# Usamos los parámetros optimizados para generar la curva de descarga
tiempos_modelo = np.linspace(min(tiempos), max(tiempos), 100)
voltajes_modelo = modelo_descarga(tiempos_modelo, Vb_estimado, RC_estimado)

# Graficamos los datos y el modelo
plt.scatter(tiempos, voltajes, label='Datos medidos')
plt.plot(tiempos_modelo, voltajes_modelo, label='Modelo de descarga', color='red')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.title('Curva de Descarga del Capacitor')
plt.legend()
plt.show()
