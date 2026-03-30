import tkinter as tk

root = tk.Tk()
root.title("Simulador de Semáforo Real")

# Canvas com fundo preto para destacar as luzes
canvas = tk.Canvas(root, width=200, height=450, bg="#1a1a1a", highlightthickness=0)
canvas.pack(pady=20)

# Desenha as luzes (inicialmente todas apagadas/cinza)
red_light = canvas.create_oval(50, 50, 150, 150, fill="#333333", outline="#555555", width=2)
yellow_light = canvas.create_oval(50, 160, 150, 260, fill="#333333", outline="#555555", width=2)
green_light = canvas.create_oval(50, 270, 150, 370, fill="#333333", outline="#555555", width=2)

# Mapeamento do ciclo real: (Cor Atual, Próximo Estado, Tempo em ms)
# Sequência: Vermelho (3s) -> Verde (3s) -> Amarelo (1.5s) -> Vermelho...
traffic_logic = {
    "red": {"next": "green", "delay": 3000, "lights": ("red", "#FF0000", "#333333", "#333333")},
    "green": {"next": "yellow", "delay": 3000, "lights": ("#333333", "#333333", "#00FF00")},
    "yellow": {"next": "red", "delay": 1500, "lights": ("#333333", "#FFFF00", "#333333")}
}

def update_semaphore(current_state):
    # Reset de todas as luzes para o tom escuro
    canvas.itemconfig(red_light, fill="#333333")
    canvas.itemconfig(yellow_light, fill="#333333")
    canvas.itemconfig(green_light, fill="#333333")
    
    # Ativa a luz correspondente ao estado atual
    if current_state == "red":
        canvas.itemconfig(red_light, fill="#FF0000")
    elif current_state == "yellow":
        canvas.itemconfig(yellow_light, fill="#FFFF00")
    elif current_state == "green":
        canvas.itemconfig(green_light, fill="#00FF00")
    
    # Pega as configurações do próximo passo
    next_state = traffic_logic[current_state]["next"]
    delay = traffic_logic[current_state]["delay"]
    
    # Agenda a próxima transição
    root.after(delay, lambda: update_semaphore(next_state))

# Inicia o ciclo pelo Vermelho
update_semaphore("red")

root.mainloop()
