class Vista:
    def mostrar_menu_principal(self):
        print("""
        Acciones disponibles:
            - Registro
            - Login
            - Salir
        """)
        return input("¿Qué quieres hacer?: ").lower()

    def mostrar_menu_notas(self):
        print("""
        Opciones disponibles:
            - Crear nota
            - Mostrar notas
            - Eliminar nota
            - Cerrar sesión
        """)
        return input("Ingresa la acción que deseas realizar: ").lower()

    def pedir_datos_registro(self):
        print("Ingresando al sistema de registro")
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña: ")
        return nombre, apellido, email, password

    def pedir_datos_login(self):
        print("Ingresando al sistema de login")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña: ")
        return email, password

    def pedir_datos_nota(self, nombre_usuario):
        print(f"{nombre_usuario}, vamos a crear una nueva nota")
        titulo = input("Ingresa el título de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota: ")
        return titulo, descripcion

    def pedir_titulo_eliminar(self, nombre_usuario):
        return input(f"{nombre_usuario}, ingresa el título de la nota que quieres borrar: ")

    def mostrar_notas(self, nombre_usuario, notas):
        print(f"{nombre_usuario}, tus notas son: ")
        for nota in notas:
            print("-------------------------------")
            print("Título: ", nota["titulo"])
            print("Contenido: ", nota["descripcion"])
            print("-------------------------------\n")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)