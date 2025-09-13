import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=400, bg="black")
canvas.pack()

# Crie os três círculos (luzes) com a cor inicial cinza
red_light = canvas.create_oval(50, 50, 150, 150, fill="grey")
yellow_light = canvas.create_oval(50, 160, 150, 260, fill="grey")
green_light = canvas.create_oval(50, 270, 150, 370, fill="grey")

# Crie uma lista com as luzes e as cores para facilitar o controle
lights = [red_light, yellow_light, green_light]
colors = ["red", "yellow", "green"]

current_light_index = 0

def change_light():
    global current_light_index
    
    # Desliga todas as luzes, definindo a cor para cinza
    for light in lights:
        canvas.itemconfig(light, fill="grey")
    
    # Acende a luz atual com a cor correta
    canvas.itemconfig(lights[current_light_index], fill=colors[current_light_index])
    
    # Avança para a próxima luz, reiniciando se chegar ao fim
    current_light_index = (current_light_index + 1) % len(lights)
    
    # Agenda a próxima troca de luz após 1000 milissegundos (1 segundo)
    root.after(1000, change_light)

# Inicia a sequência de troca de luzes
change_light()

root.mainloop()