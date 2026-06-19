import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Moderna")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.temas = {
            "Oscuro": {
                "bg": "#1E1E1E",
                "fg": "white",
                "btn": "#333333",
                "btn_fg": "white"
            },
            "Azul": {
                "bg": "#0F172A",
                "fg": "white",
                "btn": "#1E40AF",
                "btn_fg": "white"
            },
            "Verde": {
                "bg": "#052E16",
                "fg": "white",
                "btn": "#15803D",
                "btn_fg": "white"
            },
            "Claro": {
                "bg": "#F5F5F5",
                "fg": "black",
                "btn": "#D1D5DB",
                "btn_fg": "black"
            }
        }

        self.expresion = tk.StringVar()

        self.crear_interfaz()
        self.cambiar_tema("Oscuro")

    def crear_interfaz(self):

        self.frame_top = tk.Frame(self.root)
        self.frame_top.pack(fill="x", pady=10)

        ttk.Label(
            self.frame_top,
            text="Tema:"
        ).pack(side="left", padx=10)

        self.combo_tema = ttk.Combobox(
            self.frame_top,
            values=list(self.temas.keys()),
            state="readonly"
        )
        self.combo_tema.current(0)
        self.combo_tema.pack(side="left")

        self.combo_tema.bind(
            "<<ComboboxSelected>>",
            lambda e: self.cambiar_tema(self.combo_tema.get())
        )

        self.pantalla = tk.Entry(
            self.root,
            textvariable=self.expresion,
            font=("Segoe UI", 28),
            justify="right",
            bd=0
        )

        self.pantalla.pack(
            fill="x",
            padx=15,
            pady=15,
            ipady=20
        )

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(expand=True, fill="both")

        botones = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=',]
        ]

        for fila in botones:
            fila_frame = tk.Frame(self.frame_botones)
            fila_frame.pack(expand=True, fill="both")

            for texto in fila:

                if texto == "=":
                    comando = self.calcular
                elif texto == "C":
                    comando = self.limpiar
                else:
                    comando = lambda t=texto: self.agregar(t)

                btn = tk.Button(
                    fila_frame,
                    text=texto,
                    font=("Segoe UI", 18, "bold"),
                    command=comando,
                    relief="flat",
                    cursor="hand2"
                )

                btn.pack(
                    side="left",
                    expand=True,
                    fill="both",
                    padx=3,
                    pady=3
                )

    def agregar(self, valor):
        self.expresion.set(self.expresion.get() + str(valor))

    def limpiar(self):
        self.expresion.set("")

    def calcular(self):
        try:
            resultado = eval(self.expresion.get())
            self.expresion.set(str(resultado))
        except:
            self.expresion.set("Error")

    def cambiar_tema(self, nombre):

        tema = self.temas[nombre]

        self.root.configure(bg=tema["bg"])
        self.frame_top.configure(bg=tema["bg"])
        self.frame_botones.configure(bg=tema["bg"])

        self.pantalla.configure(
            bg=tema["bg"],
            fg=tema["fg"],
            insertbackground=tema["fg"]
        )

        for frame in self.frame_botones.winfo_children():
            frame.configure(bg=tema["bg"])

            for btn in frame.winfo_children():
                btn.configure(
                    bg=tema["btn"],
                    fg=tema["btn_fg"],
                    activebackground=tema["fg"],
                    activeforeground=tema["bg"]
                )

if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style()
    style.theme_use("clam")

    app = Calculadora(root)

    root.mainloop()