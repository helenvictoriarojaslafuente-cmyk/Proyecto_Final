# ------------- Bloque 1 ----------------
# Diccionario de usuarios registrados
usuarios = {
    "helen": "2001"  
    # Cambiado a minúscula para coincidir con lower()
}

while True:
    print("""
Bienvenida al Sistema Clínico!!!
    Por favor Selecciona una Opción:
    1. Iniciar Sesión
    2. Registrarse
    3. Recuperar Contraseña
    4. Salir del sistema""")

    opcion = input("Ingrese el número de la opción que desea: ").strip()

    if opcion == "1":
        print("Iniciar Sesión")
        while True:
            nombre = input("Ingrese su nombre de usuario: ").strip().lower()
            contrasena = input("Ingrese su contraseña: ").strip()
            # Verifica contra el diccionario, no hardcodeado
            if nombre in usuarios and usuarios[nombre] == contrasena:
                print(f"Inicio de sesión exitoso. ¡Bienvenida, {nombre}!")
                break
            else:
                print("Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")

    elif opcion == "2":
        print("Registrarse")
        nuevo_usuario = input("Ingrese un nombre de usuario para registrarse: ").strip().lower()
        if nuevo_usuario in usuarios:
            print("Ese nombre de usuario ya existe. Por favor elija otro.")
        else:
            nueva_contrasena = input("Ingrese una contraseña para registrarse: ").strip()
            # Guarda el nuevo usuario en el diccionario
            usuarios[nuevo_usuario] = nueva_contrasena
            print(f"Registro exitoso. ¡Bienvenida, {nuevo_usuario}! Ya puede iniciar sesión.")

    elif opcion == "3":
        print("Recuperar Contraseña")
        correo = input("Ingrese su correo electrónico para recuperar su contraseña: ").strip().lower()
        print("Se ha enviado un enlace de recuperación a su correo electrónico.")

    elif opcion == "4":
        print("Saliendo del sistema. ¡Gracias por usar el Sistema Clínico, Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
