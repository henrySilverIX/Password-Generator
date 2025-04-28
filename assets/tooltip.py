import tkinter

class Tooltip:
    def __init__(self, widget, texto):
        self.widget = widget
        self.texto = texto
        self.tooltip = None
        widget.bind("<Enter>", self.mostrar)
        widget.bind("<Leave>", self.esconder)

    def mostrar(self, event=None):
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() - 20
        self.tooltip = tkinter.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)  # Tira a borda da janela
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tkinter.Label(self.tooltip, text=self.texto, background="yellow", relief="solid", borderwidth=1, font=("Arial", 10))
        label.pack()

    def esconder(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None