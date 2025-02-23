import hashlib
from datetime import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, email, password, es_cifrada=False):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password if es_cifrada else self.cifrar_password(password)
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def cifrar_password(self, password):
        cifrado = hashlib.sha256()
        cifrado.update(password.encode('utf8'))
        return cifrado.hexdigest()

    def verificar_password(self, password):
        return self.password == self.cifrar_password(password)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "password": self.password,
            "fecha": self.fecha
        }