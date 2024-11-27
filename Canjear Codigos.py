import pydirectinput
import pyautogui
import time
import pyperclip

INPUT_COORDS = (1100, 470)
SUBMIT_COORDS = (1270, 630)
CODES_FILE = "Archivos de Texto/codes.txt"

try:
    with open(CODES_FILE, "r", encoding="utf-8") as file:
        codes = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print(f"El archivo '{CODES_FILE}' no se encontró. Asegúrate de que la ruta sea correcta.")
    exit()

for index, code in enumerate(codes):
    print(f"Procesando código {index + 1}: {code}")
    pydirectinput.doubleClick(*INPUT_COORDS)
    
    pyperclip.copy(code)
    pyautogui.hotkey("ctrl", "v")
    
    time.sleep(0.5)
    pydirectinput.click(*SUBMIT_COORDS)
    time.sleep(3)

print("Todos los códigos han sido procesados.")
