# Autor
Camilo Esteban Ramirez Salas :smile:

# Gestor de Notas

Esta aplicación consiste en un Gestor de Notas, es una aplicación de línea de comandos desarrollada en Python que permite a los usuarios registrarse, iniciar sesión, crear, ver y eliminar notas. La persistencia de datos se maneja mediante archivos JSON, lo que elimina la necesidad de una base de datos tradicional.

## Características

- **Registro de Usuarios**: Los usuarios pueden registrarse proporcionando su nombre, apellido, email y contraseña.
- **Inicio de Sesión**: Los usuarios registrados pueden iniciar sesión con su email y contraseña.
- **Gestión de Notas**:
  - **Crear Notas**: Los usuarios pueden crear nuevas notas con un título y una descripción.
  - **Mostrar Notas**: Los usuarios pueden ver todas sus notas.
  - **Eliminar Notas**: Los usuarios pueden eliminar notas específicas por título.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

    GestorNotasJSON/
        data/
            usuarios.json
            notas.json
        notas/
            init.py
            modelo.py      
            repositorio.py 
            acciones.py    
        usuarios/
            init.py
            modelo.py       
            repositorio.py  
            acciones.py 
        usuarios/
            init.py 
            vista.py       
        main.py
        README.md



- **data/**: Contiene los archivos JSON que almacenan los datos de los usuarios (`usuarios.json`) y las notas (`notas.json`).
- **notas/**: Módulo para la gestión de notas.
  - `modelo.py`: Contiene la clase `Nota` con su lógica pura.
  - `repositorio.py`: Maneja la lectura y escritura de notas en `notas.json`.
  - `acciones.py`: Actúa como presentador, coordinando las acciones de notas entre el modelo y la vista.
- **usuarios/**: Módulo para la gestión de usuarios.
  - `modelo.py`: Contiene la clase `Usuario` con su lógica pura, incluyendo cifrado de contraseñas.
  - `repositorio.py`: Maneja la lectura y escritura de usuarios en `usuarios.json`.
  - `acciones.py`: Actúa como presentador, coordinando las acciones de usuarios entre el modelo y la vista.
- **vista/**: Contiene la lógica de interacción con el usuario.
  - `vista.py`: Define la interfaz de línea de comandos (inputs y outputs).
- **main.py**: Punto de entrada de la aplicación, inicializa los componentes y ejecuta el programa.

## Requisitos

- Python 3.x

## Configuración

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tuusuario/tuproyecto.git
2. **Crear Archivos JSON**:
Asegúrate de que los archivos `usuarios.json` y `notas.json` existan y estén inicializados como listas vacías `[]`, sino, estando en la carpeta `data/` utiliza este comando para inicializarlos.
   ```bash
   echo '[]' > usuarios.json
   echo '[]' > notas.json

3. **Ejecución**: Estando en la carpeta raiz del proyecto, utiliza el siguiente comando.
    ```python
   python main.py