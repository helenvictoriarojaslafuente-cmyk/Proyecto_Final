citas_agendadas = ""
cantidad_citas = 0
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

# ------------- Bloque 2 ----------------
while True:
    print("""Menú Principal del Sistema Clínico
    1. Agendar Cita
    2. Ver Citas Agendadas
    3. Cancelar Cita
    4. Salir""") 
    opcion = input("Ingrese el número de la opción que desea: ").strip()
    if opcion == "1":
        print("Agendar Cita")
        fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ").strip()
        hora = input("Ingrese la hora de la cita (HH:MM): ").strip()
        # Guardar la cita en la lista
        citas_agendadas += f"{fecha} a las {hora}\n"
        cantidad_citas += 1
        print(f"Cita agendada para el {fecha} a las {hora}.")
    elif opcion == "2":
        print("Ver Citas Agendadas")
        # Verificar si hay citas agendadas
        if citas_agendadas == "":
            print("No hay citas agendadas.")
        else:
            print("Total de citas:", cantidad_citas)
            print(citas_agendadas)    
    elif opcion == "3":
        print("Cancelar Cita")
        fecha = input("Ingrese la fecha de la cita a cancelar (DD/MM/AAAA): ").strip()
        hora = input("Ingrese la hora de la cita a cancelar (HH:MM): ").strip()
        cita_a_borrar = fecha + " a las " + hora 
        citas_agendadas = citas_agendadas.replace(cita_a_borrar, "")
        cantidad_citas = cantidad_citas - 1
        print(f"Cita del {fecha} a las {hora} cancelada.")
    elif opcion == "4":
        print("Saliendo del sistema. ¡Gracias por usar el Sistema Clínico, Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
