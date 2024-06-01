import pyautogui
import time
import keyboard

#para que esta parte funcione, se debe tener google abierto en la ventana de la izquierda
#time.sleep(2)
print("\nQué desea buscar?")
Mensaje = input()

print("\nDónde desea buscar?\n1. Wikipedia.\n2. YouTube.\n3. Stack Overflow\n4. PC")
Respuesta=input()

match Respuesta:
    case "1":
         print(pyautogui.position())
         pyautogui.click(921, 1052)
         pyautogui.click(787, 930)
         pyautogui.click(504, 70)
         pyautogui.typewrite("https://es.wikipedia.org/wiki/Wikipedia:Portada")
         pyautogui.typewrite(["enter"])
         time.sleep(1.5)
         pyautogui.click(600, 190)
         pyautogui.typewrite(Mensaje)
         pyautogui.typewrite(["enter"])
    case "2":
         print("\nDesea abrir el primer video?\n1. Sí.\n2. No.")
         RespDos=input()
         print(pyautogui.position())
         pyautogui.click(921, 1052)
         pyautogui.click(787, 930)
         pyautogui.click(504, 67)
         pyautogui.typewrite("https://www.youtube.com/")
         pyautogui.typewrite(["enter"])
         time.sleep(2.8)
         pyautogui.click(562, 141)
         pyautogui.typewrite(Mensaje)
         pyautogui.typewrite(["enter"])
         time.sleep(1.5)
         if RespDos == "1": pyautogui.click(521, 566)
    case "3":
         print(pyautogui.position())
         pyautogui.click(921, 1052)
         pyautogui.click(787, 930)
         pyautogui.click(504, 67)
         pyautogui.typewrite("https://stackoverflow.com/questions/")
         pyautogui.typewrite(["enter"])
         time.sleep(1.5)
         pyautogui.click(698, 143)
         pyautogui.typewrite(Mensaje)
         pyautogui.typewrite(["enter"])
    case "4":
         print("\nDesea abrir el primer resultado?\n1. Sí.\n2. No.")
         RespDos=input()
         print(pyautogui.position())
         pyautogui.click(123, 1055)
         pyautogui.click(145, 993)
         pyautogui.typewrite(Mensaje)
         time.sleep(0.3)
         if RespDos == "1": pyautogui.click(111, 303)
    case _:
        print("Respuesta no válida.")

#im1 = pyautogui.screenshot()
#im1.save('my_screenshot.png')