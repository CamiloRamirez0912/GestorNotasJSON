import tkinter as tk
from usuarios.acciones import AccionesUsuarios
from notas.acciones import AccionesNotas
from vista.vista import VistaGUI

def main():
    root = tk.Tk()
    vista = VistaGUI(root)
    presentador_usuarios = AccionesUsuarios()
    presentador_notas = AccionesNotas()
    vista.set_presentadores(presentador_usuarios, presentador_notas)
    root.mainloop()

if __name__ == "__main__":
    main()