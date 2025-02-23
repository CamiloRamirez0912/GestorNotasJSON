import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("Ingresando al sistema de registro")
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña: ")
        
        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"Te has registrado con el email {registro[1]['email']}")
        else:
            print("No te registraste correctamente")
        
    def login(self):
        print("Ingresando al sistema de login")
        try:
            email = input("Ingresa tu email: ")
            password = input("Ingresa tu contraseña: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()
            if login:
                print(f"Bienvenido {login['nombre']}, te has registrado en el sistema el dia {login['fecha']}")
                return login
            else:
                print("El correo o contraseña son incorrectos.")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def proximasAcciones(self, usuario):
        make = notas.acciones.Acciones()
        while True:
            print("""
            Opciones disponibles:
                - Crear nota
                - Mostrar notas
                - Eliminar nota
                - Cerrar sesión
            """)
            accion = input("Ingresa la acción que deseas realizar: ").lower()
            
            if accion == "crear":
                make.crear(usuario)
            elif accion == "mostrar":
                make.mostrar(usuario)
            elif accion == "eliminar":
                make.borrar(usuario)
            elif accion == "cerrar sesion":
                print(f"Cerrando sesión de {usuario['nombre']}...")
                break 
            else:
                print("Acción no reconocida, por favor intenta de nuevo.")