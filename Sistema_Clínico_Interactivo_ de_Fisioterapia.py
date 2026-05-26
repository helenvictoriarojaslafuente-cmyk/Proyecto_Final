print("""Bienvenida al Sistema Clínico!!!
      Por favor Selecciona una Opción:
      1. Iniciar Sesión
      2. Registrarse
      3. Contraseña
      4. Salir del sistema""")
opcion = input("Ingrese el número de la opción que desea: ")
if opcion == "1":
    print("Iniciar Sesión")
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == "Helen" and contraseña == "2001":
             print("Inicio de sesión exitoso. Bienvenida, Helen!")
             break
        else: print("Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
elif opcion == "2":
    print("Registrarse")
    nuevo_usuario = input("Ingrese un nombre de usuario para registrarse: ")
    nueva_contraseña = input("Ingrese una contraseña para regístrarse: ")
    print("Registro exitoso. Ahora puede iniciar sesión con su nuevo usuario. ")
elif opcion == "3":
    print("Recuperar Contraseña")
    correo = input("Ingrese su correo electrónico para recuperar su contraseña: ")
    print("Se ha envíado un enlace de recuperación a su correo electrónico. Por favor, revise su bandeja de entrada.")
elif opcion == "4":
    print("Saliendo del sistema. ¡Gracias por usar el Sistema Clínico, Hasta luego!")
else: print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")