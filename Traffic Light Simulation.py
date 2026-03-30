import tkinter as tk

root = tk.Tk()
root.title("Simulador de Semáforo Real")

# Canvas com fundo escuro e moderno
canvas = tk.Canvas(root, width=250, height=550, bg="#1a1a1a", highlightthickness=0)
canvas.pack(pady=20)

# Desenha as luzes
red_light = canvas.create_oval(75, 50, 175, 150, fill="#333333", outline="#555555", width=2)
yellow_light = canvas.create_oval(75, 160, 175, 260, fill="#333333", outline="#555555", width=2)
green_light = canvas.create_oval(75, 270, 175, 370, fill="#333333", outline="#555555", width=2)

# Temporizador visual
timer_text = canvas.create_text(125, 450, text="", fill="white", font=("Courier New", 40, "bold"))
label_text = canvas.create_text(125, 500, text="PRÓXIMA TROCA", fill="#888888", font=("Arial", 10, "bold"))

# Lógica de tempos (em segundos para facilitar a contagem)
traffic_logic = {
    "red": {"next": "green", "duration": 3, "color": "#FF0000"},
    "green": {"next": "yellow", "duration": 5, "color": "#00FF00"},
    "yellow": {"next": "red", "duration": 1.5, "color": "#FFFF00"}
}

def update_semaphore(state, time_left):
    # 1. Atualiza as luzes visuais
    canvas.itemconfig(red_light, fill="#FF0000" if state == "red" else "#333333")
    canvas.itemconfig(yellow_light, fill="#FFFF00" if state == "yellow" else "#333333")
    canvas.itemconfig(green_light, fill="#00FF00" if state == "green" else "#333333")
    
    # 2. Atualiza o texto do contador
    # Usamos f-string para lidar com o 1.5 do amarelo
    display_time = int(time_left) if time_left % 1 == 0 else time_left
    canvas.itemconfig(timer_text, text=str(display_time), fill=traffic_logic[state]["color"])
    
    # 3. Lógica de contagem
    if time_left > 0.5: # Continua subtraindo se houver tempo
        # Subtrai de 1 em 1 segundo (ou 0.5 para precisão do amarelo)
        new_time = time_left - 1 if time_left > 1 else 0
        if state == "yellow" and time_left == 1.5:
             root.after(500, lambda: update_semaphore(state, 1.0))
        else:
             root.after(1000, lambda: update_semaphore(state, new_time))
    else:
        # Quando o tempo zera, pula para o próximo estado
        next_state = traffic_logic[state]["next"]
        new_duration = traffic_logic[next_state]["duration"]
        update_semaphore(next_state, new_duration)

# Inicia o ciclo
update_semaphore("red", traffic_logic["red"]["duration"])

root.mainloop()
