import tkinter as tk

# Criando janela
janela = tk.Tk()
janela.title("Semáforo")
janela.geometry("300x400")

# Canvas para desenhar
canvas = tk.Canvas(janela, width=200, height=350, bg="black")
canvas.pack(pady=20)

# Luzes do semáforo
vermelho = canvas.create_oval(50, 30, 150, 130, fill="gray")
amarelo = canvas.create_oval(50, 140, 150, 240, fill="gray")
verde = canvas.create_oval(50, 250, 150, 350, fill="gray")


# Funções das cores
def ligar_vermelho():
    canvas.itemconfig(vermelho, fill="red")
    canvas.itemconfig(amarelo, fill="gray")
    canvas.itemconfig(verde, fill="gray")

    janela.after(3000, ligar_amarelo)


def ligar_amarelo():
    canvas.itemconfig(vermelho, fill="gray")
    canvas.itemconfig(amarelo, fill="yellow")
    canvas.itemconfig(verde, fill="gray")

    janela.after(2000, ligar_verde)


def ligar_verde():
    canvas.itemconfig(vermelho, fill="gray")
    canvas.itemconfig(amarelo, fill="gray")
    canvas.itemconfig(verde, fill="green")

    janela.after(3000, ligar_vermelho)


# Iniciar ciclo
ligar_vermelho()

# Rodar programa
janela.mainloop()