from usuarios.acciones import AccionesUsuarios
from vista.vista import Vista

def main():
    vista = Vista()
    acciones = AccionesUsuarios()
    
    while True:
        accion = vista.mostrar_menu_principal()
        if accion == "registro":
            acciones.registro(vista)
        elif accion == "login":
            usuario = acciones.login(vista)
            if usuario:
                acciones.proximas_acciones(usuario, vista)
        elif accion == "salir":
            vista.mostrar_mensaje("Saliendo del programa...")
            break
        else:
            vista.mostrar_mensaje("Acción no reconocida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()