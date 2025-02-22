import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"{usuario['nombre']}, vamos a crear una nueva nota")
        titulo = input("Ingresa el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota: ")
        nota = modelo.Nota(usuario['id'], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"Se ha guardado correctamente la nota con titulo: {nota.titulo}")
        else:
            print("No se pudo guardar la nota.")
            
    def mostrar(self, usuario):
        print(f"{usuario['nombre']}, tus notas son: ")
        nota = modelo.Nota(usuario['id'])
        notas = nota.listar()
        for nota in notas:
            print ("-------------------------------")
            print("Titulo: ", nota["titulo"])
            print("Contenido: ", nota["descripcion"])
            print ("-------------------------------\n")
            
    def borrar(self, usuario):
        titulo = input(f"{usuario['nombre']}, ingresa el titulo de la nota que quieres borrar: ")
        nota = modelo.Nota(usuario['id'])
        eliminar = nota.eliminar(titulo)
        if eliminar[0] >= 1:
            print(f"Se ha eliminado la nota con titulo: {titulo}")
        else:
            print("No se pudo borrar la nota.")