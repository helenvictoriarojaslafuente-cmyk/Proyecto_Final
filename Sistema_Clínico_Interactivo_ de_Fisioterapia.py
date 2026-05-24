contrasena_correcta = "fisio2026"
acceso_concedido = False
while not acceso_concedido:
    intento_clave = input("Ingrese la contraseña del gabinete: ").strip()    
    if intento_clave == contrasena_correcta:
        print("\n¡Acceso concedido al sistema clínico!")
        acceso_concedido = True
    else:
        print("Contraseña incorrecta. Intente de nuevo.\n")