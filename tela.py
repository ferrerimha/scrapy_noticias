import tkinter as tk

class Tela:

    def __init__(self, tamanho, title):
        self.tamanho = tamanho
        self.title = title

    def create_display(self, textos):
        self.display = tk.Tk()
        self.display.title(self.title)
        self.display.geometry(self.tamanho)

        label = tk.Label(self.display, text="Noticias da bolha tech", font=("Arial", 14))
        label.pack(pady=60)

        frame = tk.Frame(self.display)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        texto = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        texto.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=texto.yview)

        texto.insert(tk.END, textos)

        self.display.mainloop()

