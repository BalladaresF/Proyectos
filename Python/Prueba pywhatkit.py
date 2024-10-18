import pywhatkit
import time
import pyautogui
import keyboard as k

print("Escriba el mensaje que desea enviar:")
Mensaje = input()

#pywhatkit.sendwhatmsg_to_group("Lja0hmLXbbC05cQpdJXd7T", Mensaje, 8, 38, 30, True, 5)
pywhatkit.sendwhatmsg_to_group_instantly("Lja0hmLXbbC05cQpdJXd7T", Mensaje)
pyautogui.click(1050, 950)
time.sleep(2)
k.press_and_release('enter')
