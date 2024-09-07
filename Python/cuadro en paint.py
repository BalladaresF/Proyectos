#ejecutar este código y abrir paint. Luego de unos segundos, el mouse comenzará a crear un cuadro. 

import pyautogui, time

time.sleep(5)
pyautogui.click()    # click para usar paint.
distancia = 200

while distancia > 0:
    pyautogui.dragRel(distancia, 0, duracion=0.2)   # Derecha
    distancia = distancia - 5
    pyautogui.dragRel(0, distancia, duracion=0.2)   # Abajo
    pyautogui.dragRel(-distancia, 0, duracion=0.2)  # Izquierda
    distancia = distancia - 5
    pyautogui.dragRel(0, -distancia, duracion=0.2)  # Arriba
    