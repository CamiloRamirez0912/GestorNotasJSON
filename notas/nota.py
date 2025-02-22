import json
from datetime import datetime

class Nota:
    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        
    def guardar(self):
        nueva_nota = {
            "usuario_id": self.usuario_id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        with open('data/notas.json', 'r+') as file:
            notas = json.load(file)
            notas.append(nueva_nota)
            file.seek(0)
            json.dump(notas, file, indent=4)
        
        return [1, self]
    
    def listar(self):
        with open('data/notas.json', 'r') as file:
            notas = json.load(file)
            return [nota for nota in notas if nota["usuario_id"] == self.usuario_id]
    
    def eliminar(self, titulo):
        with open('data/notas.json', 'r') as file:
            notas = json.load(file)
        
        notas_filtradas = [nota for nota in notas if not (nota["usuario_id"] == self.usuario_id and nota["titulo"] == titulo)]
        
        with open('data/notas.json', 'w') as file:
            json.dump(notas_filtradas, file, indent=4)
        
        return [1, self]