#Este es un ejemplo simple de machine learning con redes neuronales, utilizando tensorflow y keras.
#Para ello, se convierten valores de celcius a fahrenheit sin establecerle al programa la fórmula.

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#valores que se insertan a la red neuronal:
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

#ejemplo con una neurona:
#capa = tf.keras.layers.Dense(units=1, input_shape=[1]) #las capas densas tienen conexiones a todas las neuronas.
#modelo = tf.keras.Sequential([capa])

#ejemplo con tres neuronas y una capa intermedia:
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1), #con cambios finos, el sistema tarda más pero es más preciso
    loss='mean_squared_error'
)

print("\nComenzando entrenamiento. . .")
#entrenamiento óptimo de una neurona:
#historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False) #se asignan los valores de entrada y los resultados esperados, junto con la cantidad de ciclos que se van a realizar.

#entrenamiento óprimo de tres neutonas:
historial = modelo.fit(celsius, fahrenheit, epochs=200, verbose=False) #se asignan los valores de entrada y los resultados esperados, junto con la cantidad de ciclos que se van a realizar.
print("Modelo entrenado!")

plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()
  
#Ejemplo con 100 grados celcius (resultado: aprox. 212 F)
#print("- -Predicción- -")
#Resultado=modelo.predict([100.0])
#print("El resultado de 100C a Fahrenheit es: "+str(Resultado)+"F.")

#print("\nVariables internas del modelo")

#sesgos de una neurona:
#print(capa.get_weights())
#sesgos de tres neuronas y una capa intermedia:
#print(oculta1.get_weights())
#print(oculta2.get_weights())
#print(salida.get_weights())

#por último, se ingresa cualquier valor C para convertirse a F
print("\nIngrese grados en celsius para convertirlos a fahrenheit:")
Valor=input()
Resul2=modelo.predict([float(Valor)])
print(Valor+"C a fahrenheit es: "+str(Resul2)+"F.\n")