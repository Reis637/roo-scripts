import pydirectinput
import time
from pynput import keyboard

PLANTAR_COORDS = (1670, 810)
ACELERAR_COORDS = (1570, 690)
COSECHAR_COORDS = (1670, 810)

STOP = False
CICLOS = 30

def cuenta_regresiva(segundos):
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)

def ejecutar_accion(coords, delay=0.5):
    x, y = coords
    pydirectinput.click(x, y)
    time.sleep(delay)

def detener_script(key):
    global STOP
    if key == keyboard.Key.esc:
        STOP = True
        return False

def main():
    global STOP

    cuenta_regresiva(5)

    with keyboard.Listener(on_press=detener_script):
        for ciclo in range(CICLOS):
            if STOP:
                print("Script detenido por el usuario.")
                break

            print(f"Ciclo {ciclo + 1} de {CICLOS}")

            ejecutar_accion(PLANTAR_COORDS, delay=2)
            ejecutar_accion(ACELERAR_COORDS, delay=0.5)
            ejecutar_accion(COSECHAR_COORDS, delay=2)

        print("Proceso completado.")

if __name__ == "__main__":
    main()
