from notas.modelo import Nota
from notas.repositorio import NotasRepository

class AccionesNotas:
    def __init__(self, repositorio=NotasRepository()):
        self.repositorio = repositorio

    def crear(self, usuario, vista):
        titulo, descripcion = vista.pedir_datos_nota(usuario.nombre)
        nota = Nota(usuario.id, titulo, descripcion)
        if self.repositorio.guardar(nota):
            vista.mostrar_mensaje(f"Se ha guardado correctamente la nota con título: {titulo}")
        else:
            vista.mostrar_mensaje("No se pudo guardar la nota.")

    def mostrar(self, usuario, vista):
        notas = self.repositorio.listar(usuario.id)
        vista.mostrar_notas(usuario.nombre, notas)

    def borrar(self, usuario, vista):
        titulo = vista.pedir_titulo_eliminar(usuario.nombre)
        if self.repositorio.eliminar(usuario.id, titulo):
            vista.mostrar_mensaje(f"Se ha eliminado la nota con título: {titulo}")
        else:
            vista.mostrar_mensaje("No se pudo borrar la nota.")