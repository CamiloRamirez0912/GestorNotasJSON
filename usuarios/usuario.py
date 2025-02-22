import json
import hashlib
from datetime import datetime

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        password_cifrada = cifrado.hexdigest()
        
        nuevo_usuario = {
            "id": self.generar_id(),
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "password": password_cifrada,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        with open('data/usuarios.json', 'r+') as file:
            usuarios = json.load(file)
            usuarios.append(nuevo_usuario)
            file.seek(0)
            json.dump(usuarios, file, indent=4)
        
        return [1, nuevo_usuario]
    
    def identificar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        password_cifrada = cifrado.hexdigest()
        
        with open('data/usuarios.json', 'r') as file:
            usuarios = json.load(file)
            for usuario in usuarios:
                if usuario["email"] == self.email and usuario["password"] == password_cifrada:
                    return usuario
        return None
    
    def generar_id(self):
        with open('data/usuarios.json', 'r') as file:
            usuarios = json.load(file)
            return len(usuarios) + 1