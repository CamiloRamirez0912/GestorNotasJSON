import json
from usuarios.modelo import Usuario

class UsuariosRepository:
    def __init__(self, archivo="data/usuarios.json"):
        self.archivo = archivo

    def guardar(self, usuario):
        with open(self.archivo, 'r+') as file:
            usuarios = json.load(file)
            usuarios.append(usuario.to_dict())
            file.seek(0)
            json.dump(usuarios, file, indent=4)
        return True

    def identificar(self, email, password):
        with open(self.archivo, 'r') as file:
            usuarios = json.load(file)
            for u in usuarios:
                usuario = Usuario(u["id"], u["nombre"], u["apellido"], u["email"], u["password"], es_cifrada=True)
                if u["email"] == email and usuario.verificar_password(password):
                    return usuario
        return None

    def generar_id(self):
        with open(self.archivo, 'r') as file:
            usuarios = json.load(file)
            return len(usuarios) + 1