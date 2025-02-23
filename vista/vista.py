import tkinter as tk
from tkinter import messagebox, ttk

class VistaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Notas")
        self.root.geometry("500x400")
        self.usuario_actual = None
        self.presentador_usuarios = None
        self.presentador_notas = None

    def set_presentadores(self, presentador_usuarios, presentador_notas):
        self.presentador_usuarios = presentador_usuarios
        self.presentador_notas = presentador_notas
        self.mostrar_menu_principal()

    def mostrar_menu_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Bienvenido al Gestor de Notas", font=("Arial", 16)).pack(pady=20)

        btn_config = {
            "font": ("Arial", 12),  
            "width": 15,            
            "height": 2,            
            "padx": 10,             
            "pady": 5               
        }

        tk.Button(self.root, text="Registro", command=self.mostrar_registro, **btn_config).pack(pady=10)
        tk.Button(self.root, text="Login", command=self.mostrar_login, **btn_config).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit, **btn_config).pack(pady=10)

    def mostrar_registro(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Registro", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        tk.Label(self.root, text="Apellido:").pack()
        self.entry_apellido = tk.Entry(self.root)
        self.entry_apellido.pack()

        tk.Label(self.root, text="Email:").pack()
        self.entry_email_reg = tk.Entry(self.root)
        self.entry_email_reg.pack()

        tk.Label(self.root, text="Contraseña:").pack()
        self.entry_pass_reg = tk.Entry(self.root, show="*")
        self.entry_pass_reg.pack()

        tk.Button(self.root, text="Registrar", command=self.registrar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu_principal).pack(pady=10)

    def mostrar_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Email:").pack()
        self.entry_email_login = tk.Entry(self.root)
        self.entry_email_login.pack()

        tk.Label(self.root, text="Contraseña:").pack()
        self.entry_pass_login = tk.Entry(self.root, show="*")
        self.entry_pass_login.pack()

        tk.Button(self.root, text="Iniciar Sesión", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu_principal).pack(pady=10)

    def mostrar_menu_notas(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Bienvenido, {self.usuario_actual.nombre}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Crear Nota", command=self.crear_nota).pack(pady=5)
        tk.Button(self.root, text="Mostrar Notas", command=self.mostrar_notas).pack(pady=5)
        tk.Button(self.root, text="Eliminar Nota", command=self.eliminar_nota).pack(pady=5)
        tk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=5)

    def registrar(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        email = self.entry_email_reg.get()
        password = self.entry_pass_reg.get()
        self.presentador_usuarios.registro(self, nombre, apellido, email, password)

    def login(self):
        email = self.entry_email_login.get()
        password = self.entry_pass_login.get()
        usuario = self.presentador_usuarios.login(self, email, password)
        if usuario:
            self.usuario_actual = usuario
            self.mostrar_menu_notas()

    def crear_nota(self):
        ventana_nueva = tk.Toplevel(self.root)
        ventana_nueva.title("Crear Nota")
        ventana_nueva.geometry("400x300")

        tk.Label(ventana_nueva, text="Título:").pack()
        entry_titulo = tk.Entry(ventana_nueva)
        entry_titulo.pack()

        tk.Label(ventana_nueva, text="Descripción:").pack()
        entry_desc = tk.Text(ventana_nueva, height=5, width=30)
        entry_desc.pack()

        tk.Button(ventana_nueva, text="Guardar", command=lambda: [
            self.presentador_notas.crear(self.usuario_actual, self, entry_titulo.get(), entry_desc.get("1.0", tk.END).strip()),
            ventana_nueva.destroy()
        ]).pack(pady=10)

    def mostrar_notas(self):
        ventana_notas = tk.Toplevel(self.root)
        ventana_notas.title("Mis Notas")
        ventana_notas.geometry("500x400")

        notas = self.presentador_notas.mostrar(self.usuario_actual, self)
        if not notas:
            tk.Label(ventana_notas, text="No hay notas para mostrar.").pack(pady=20)
        else:
            tree = ttk.Treeview(ventana_notas, columns=("Título", "Descripción"), show="headings")
            tree.heading("Título", text="Título")
            tree.heading("Descripción", text="Descripción")
            tree.pack(fill=tk.BOTH, expand=True)

            for nota in notas:
                tree.insert("", tk.END, values=(nota["titulo"], nota["descripcion"]))

    def eliminar_nota(self):
        ventana_eliminar = tk.Toplevel(self.root)
        ventana_eliminar.title("Eliminar Nota")
        ventana_eliminar.geometry("300x150")

        tk.Label(ventana_eliminar, text="Título de la nota a eliminar:").pack()
        entry_titulo = tk.Entry(ventana_eliminar)
        entry_titulo.pack()

        tk.Button(ventana_eliminar, text="Eliminar", command=lambda: [
            self.presentador_notas.borrar(self.usuario_actual, self, entry_titulo.get()),
            ventana_eliminar.destroy()
        ]).pack(pady=10)

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.mostrar_menu_principal()

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def pedir_datos_registro(self):
        pass

    def pedir_datos_login(self):
        pass

    def pedir_datos_nota(self, nombre_usuario):
        pass

    def pedir_titulo_eliminar(self, nombre_usuario):
        pass