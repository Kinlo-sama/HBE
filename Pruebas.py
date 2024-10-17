import time
import os

def clear_terminal():
    # Comando para limpiar la terminal (funciona en Windows y Unix-like)
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_square(step):
    size = 5  # Tamaño del cuadrado
    square = []

    for i in range(size):
        if i == 0 or i == size - 1:
            if step >= i + 1:
                square.append("+" + "-" * (size - 2) + "+")  # Bordes superiores e inferiores
            else:
                square.append(" " * size)  # Espacio vacío antes de completar la línea
        else:
            if step >= size - 1:  # Lados del cuadrado
                square.append("|" + " " * (size - 2) + "|")
            else:
                square.append(" " * size)  # Espacio vacío antes de completar la línea

    # Mostrar solo las líneas hasta el paso actual
    for line in square[:step]:
        print(line)

# Simulación de dibujo paso a paso
for step in range(1, 7):
    clear_terminal()
    draw_square(step)
    time.sleep(0.5)  # Pausa para simular la animación

