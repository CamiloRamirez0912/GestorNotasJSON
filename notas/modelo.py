from datetime import datetime

class Nota:
    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha": self.fecha
        }