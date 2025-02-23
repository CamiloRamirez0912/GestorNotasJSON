from usuarios import acciones

def main():
    while True:
        print("""
        Acciones disponibles:
            - Registro
            - Login
            - Salir
        """)

        accion = input("¿Qué quieres hacer?: ").lower()
        make = acciones.Acciones()

        if accion == "registro":
            make.registro()
        elif accion == "login":
            usuario = make.login()
            if usuario:
                make.proximasAcciones(usuario)
        elif accion == "salir":
            print("Saliendo del programa...")
            break
        else:
            print("Acción no reconocida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()