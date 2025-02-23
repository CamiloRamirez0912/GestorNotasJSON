from usuarios.modelo import Usuario
from usuarios.repositorio import UsuariosRepository
from notas.acciones import AccionesNotas

class AccionesUsuarios:
    def __init__(self, repositorio=UsuariosRepository()):
        self.repositorio = repositorio
        self.acciones_notas = AccionesNotas()

    def registro(self, vista):
        nombre, apellido, email, password = vista.pedir_datos_registro()
        usuario = Usuario(self.repositorio.generar_id(), nombre, apellido, email, password)  # Sin es_cifrada, se cifra aquí
        if self.repositorio.guardar(usuario):
            vista.mostrar_mensaje(f"Te has registrado con el email {email}")
        else:
            vista.mostrar_mensaje("No te registraste correctamente")

    def login(self, vista):
        email, password = vista.pedir_datos_login()
        usuario = self.repositorio.identificar(email, password)
        if usuario:
            vista.mostrar_mensaje(f"Bienvenido {usuario.nombre}, te has registrado el día {usuario.fecha}")
            return usuario
        else:
            vista.mostrar_mensaje("El correo o contraseña son incorrectos.")
            return None

    def proximas_acciones(self, usuario, vista):
        while True:
            accion = vista.mostrar_menu_notas()
            if accion == "crear":
                self.acciones_notas.crear(usuario, vista)
            elif accion == "mostrar":
                self.acciones_notas.mostrar(usuario, vista)
            elif accion == "eliminar":
                self.acciones_notas.borrar(usuario, vista)
            elif accion == "cerrar sesion":
                vista.mostrar_mensaje(f"Cerrando sesión de {usuario.nombre}...")
                break
            else:
                vista.mostrar_mensaje("Acción no reconocida, por favor intenta de nuevo.")