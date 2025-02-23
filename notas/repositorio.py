import json
from notas.modelo import Nota

class NotasRepository:
    def __init__(self, archivo="data/notas.json"):
        self.archivo = archivo

    def guardar(self, nota):
        with open(self.archivo, 'r+') as file:
            notas = json.load(file)
            notas.append(nota.to_dict())
            file.seek(0)
            json.dump(notas, file, indent=4)
        return True

    def listar(self, usuario_id):
        with open(self.archivo, 'r') as file:
            notas = json.load(file)
            return [nota for nota in notas if nota["usuario_id"] == usuario_id]

    def eliminar(self, usuario_id, titulo):
        with open(self.archivo, 'r') as file:
            notas = json.load(file)
        
        notas_filtradas = [nota for nota in notas if not (nota["usuario_id"] == usuario_id and nota["titulo"] == titulo)]
        
        with open(self.archivo, 'w') as file:
            json.dump(notas_filtradas, file, indent=4)
        return len(notas) != len(notas_filtradas)