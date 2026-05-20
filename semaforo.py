import tkinter as tk


class Semaforo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Semáforo Inteligente")
        self.janela.geometry("300x500")
        self.janela.configure(bg="gray20")

        # Estado do semáforo
        self.funcionando = False

        # Título
        self.titulo = tk.Label(
            janela,
            text="SEMÁFORO",
            font=("Arial", 20, "bold"),
            bg="gray20",
            fg="white"
        )
        self.titulo.pack(pady=10)

        # Contador
        self.contador = tk.Label(
            janela,
            text="",
            font=("Arial", 18, "bold"),
            bg="gray20",
            fg="white"
        )
        self.contador.pack()

        # Área do desenho
        self.canvas = tk.Canvas(
            janela,
            width=180,
            height=350,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(pady=20)

        # Estrutura do semáforo
        self.canvas.create_rectangle(40, 20, 140, 320, fill="gray10")

        # Luzes
        self.vermelho = self.canvas.create_oval(
            55, 35, 125, 105,
            fill="gray"
        )

        self.amarelo = self.canvas.create_oval(
            55, 125, 125, 195,
            fill="gray"
        )

        self.verde = self.canvas.create_oval(
            55, 215, 125, 285,
            fill="gray"
        )

        # Botões
        self.botao_iniciar = tk.Button(
            janela,
            text="Iniciar",
            font=("Arial", 12, "bold"),
            width=10,
            command=self.iniciar
        )
        self.botao_iniciar.pack(side="left", padx=30)

        self.botao_parar = tk.Button(
            janela,
            text="Parar",
            font=("Arial", 12, "bold"),
            width=10,
            command=self.parar
        )
        self.botao_parar.pack(side="right", padx=30)

    # ---------------------------
    # Função para apagar tudo
    # ---------------------------
    def apagar_luzes(self):
        self.canvas.itemconfig(self.vermelho, fill="gray")
        self.canvas.itemconfig(self.amarelo, fill="gray")
        self.canvas.itemconfig(self.verde, fill="gray")

    # ---------------------------
    # Vermelho
    # ---------------------------
    def vermelho_on(self):
        if not self.funcionando:
            return

        self.apagar_luzes()

        self.canvas.itemconfig(self.vermelho, fill="red")

        self.contagem(5, self.amarelo_on)

    # ---------------------------
    # Amarelo
    # ---------------------------
    def amarelo_on(self):
        if not self.funcionando:
            return

        self.apagar_luzes()

        self.canvas.itemconfig(self.amarelo, fill="yellow")

        self.contagem(2, self.verde_on)

    # ---------------------------
    # Verde
    # ---------------------------
    def verde_on(self):
        if not self.funcionando:
            return

        self.apagar_luzes()

        self.canvas.itemconfig(self.verde, fill="lime")

        self.contagem(5, self.vermelho_on)

    # ---------------------------
    # Contador regressivo
    # ---------------------------
    def contagem(self, tempo, proxima_funcao):

        if not self.funcionando:
            return

        self.contador.config(text=f"Tempo: {tempo}")

        if tempo > 0:
            self.janela.after(
                1000,
                lambda: self.contagem(
                    tempo - 1,
                    proxima_funcao
                )
            )
        else:
            proxima_funcao()

    # ---------------------------
    # Iniciar
    # ---------------------------
    def iniciar(self):
        if not self.funcionando:
            self.funcionando = True
            self.vermelho_on()

    # ---------------------------
    # Parar
    # ---------------------------
    def parar(self):
        self.funcionando = False
        self.apagar_luzes()
        self.contador.config(text="Semáforo parado")


# Criar janela
janela = tk.Tk()

# Criar objeto
app = Semaforo(janela)

# Rodar programa
janela.mainloop()