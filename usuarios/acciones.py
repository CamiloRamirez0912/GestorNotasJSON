from usuarios.modelo import Usuario
from usuarios.repositorio import UsuariosRepository
from notas.acciones import AccionesNotas

class AccionesUsuarios:
    def __init__(self, repositorio=UsuariosRepository()):
        self.repositorio = repositorio
        self.acciones_notas = AccionesNotas()

    def registro(self, vista, nombre, apellido, email, password):  # Añadimos parámetros
        usuario = Usuario(self.repositorio.generar_id(), nombre, apellido, email, password)
        if self.repositorio.guardar(usuario):
            vista.mostrar_mensaje(f"Te has registrado con el email {email}")
        else:
            vista.mostrar_mensaje("No te registraste correctamente")

    def login(self, vista, email, password):  # Añadimos parámetros
        usuario = self.repositorio.identificar(email, password)
        if usuario:
            vista.mostrar_mensaje(f"Bienvenido {usuario.nombre}, te has registrado el día {usuario.fecha}")
            return usuario
        else:
            vista.mostrar_mensaje("El correo o contraseña son incorrectos.")
            return None

    def proximas_acciones(self, usuario, vista):  # No necesitamos bucle, la GUI lo maneja
        pass  # La GUI ya muestra el menú de notas