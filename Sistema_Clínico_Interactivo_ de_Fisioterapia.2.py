Pacientes = [
    {"nombre": "Juan Pérez", "lesion": "Lumbalgia Aguda", "tratamiento": "Termoterapia, Electroterapia, Masoterapia", "sesion": 3, "tiempo": "45 minutos", "costo": 100, "asistencias": 0, "faltas": 0},
    {"nombre": "Ana Martínez", "lesion": "Esguince de tobillo 1er grado", "tratamiento": "Crioterapia, Electroterapi, Kinesioterapia Pasiva", "sesion": 4, "tiempo": "30 minutos", "costo":80, "asistencias": 0, "faltas": 0},
    {"nombre": "Carlos López", "lesion": "Cefalea Tensional crónica", "tratamiento": "Termoterapia, Masoterapia Cervical, Kinesioterapia pasiva", "sesion": 6, "tiempo": "45 minutos", "costo": 110, "asistencias": 0, "faltas": 0},
    {"nombre": "Sofía Ramírez", "lesion": "Ciatica", "tratamiento": "Termoterapia, Electroterapia, Kinesioterapia pasiva", "sesion": 5, "tiempo": "45 minutos", "costo": 100, "asistencias": 0, "faltas": 0},
    {"nombre": "Miguel Torres", "lesion": "Fascitis plantar aguda", "tratamiento": "Crioterapia, Electroterapia, Masoterapia", "sesion": 4, "tiempo": "30 minutos", "costo": 90, "asistencias": 0, "faltas": 0}
    ]

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
Bienvenid@ al Sistema Clínico!!!
    Por favor Selecciona una Opción:
    1. Iniciar Sesión
    2. Registrarse
    3. Recuperar Contraseña
    4. Salir del sistema""")

    opcion = input("Ingrese el número de la opción que desea: ").strip()

    if opcion == "1":
        print("Iniciar Sesión")
        nombre = input("Ingrese su nombre de usuario: ").strip().lower()
        contrasena = input("Ingrese su contraseña: ").strip()
            # Verifica contra el diccionario, no hardcodeado
        if nombre in usuarios and usuarios[nombre] == contrasena:
            print(f"Inicio de sesión exitoso. ¡Bienvenid@, {nombre}!")
        
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
                    paciente = input("Nombre del paciente: ").strip()
                    # Variables para datos del paciente
                    lesion = ""
                    tratamiento = ""
                    sesion = 0
                    tiempo = ""
                    costo = 0
                    asistencias = 0
                    faltas = 0
                    encontrado = False
                    # Buscar si existe en la lista de Pacientes para mostrar su historial clínico, si no existe, se le pedirá ingresar los datos manualmente y se guardará en la lista de Pacientes
                    for p in Pacientes:
                        if p["nombre"].lower() == paciente.lower():
                            lesion = p["lesion"]
                            tratamiento = p["tratamiento"]
                            sesion = p["sesion"]
                            tiempo = p["tiempo"]
                            costo = p["costo"]
                            asistencias = p["asistencias"]
                            faltas = p["faltas"]
                            encontrado = True
                            # Incrementar la sesión automáticamente
                            sesion = sesion + 1
                            p["sesion"] = sesion
                            break
                    if encontrado:
                    # 1. Si el paciente ya existe: Suma la sesión y muestra el historial directo 
                        sesion = sesion + 1
                        for p in Pacientes:
                             if p["nombre"].lower() == paciente.lower(): p["sesion"] = sesion
                        # Guardar la cita del paciente registrado con su historial clínico actualizado
                        datos_paciente = f"Paciente: {paciente} Lesión: {lesion} Tratamiento: {tratamiento} Sesiones: {sesion} Duración: {tiempo} Costo: {costo} Asistencias: {asistencias} Faltas: {faltas}"
                        citas_agendadas += f"{fecha} a las {hora} [datos del paciente: {datos_paciente}]\n"
                        cantidad_citas += 1
                        print(f"Cita agendada con exito para el {fecha} a las {hora}.")
                        # Mostrar el historial clínico de forma automática
                        print("HISTORIAL CLÍNICO COMPLETO")
                        print (f"Paciente: {paciente.upper()}")
                        print(f"Tipo de Lesión: {lesion}")
                        print(f"Tratamiento: {tratamiento}")
                        print(f"Sesión actual: {sesion}")
                        print(f"Tiempo: {tiempo}")
                        print(f"Costo: {costo}")
                        print(f"Historial acumulado: {asistencias} Asistencias {faltas} faltas")
                        
                    else:
                        print(f"Paciente nuevo. Ingrese los datos manualmente.")
                        lesion = input("Lesión del paciente: ").strip()
                        tratamiento = input("Tratamiento a aplicar: ").strip()
                        sesion = int(input("Número de sesiones inicial: ").strip())
                        tiempo = input("Duración de cada sesión (ej. 30 minutos): ").strip()
                        costo = float(input("Costo por sesión: ").strip())
                        asistencias = 0
                        faltas = 0

                        nuevo_paciente = {"nombre": paciente, "lesion": lesion, "tratamiento": tratamiento, "sesion": sesion, "tiempo": tiempo, "costo": costo, "asistencias": asistencias, "faltas": faltas}
                        Pacientes += [nuevo_paciente]
                        # Guardar la cita del paciente nuevo
                        datos_paciente = f"Paciente: {paciente} Lesión: {lesion} Tratamiento: {tratamiento} Sesiones: {sesion} Duración: {tiempo} Costo: {costo} Asistencias: {asistencias} Faltas: {faltas}"
                        citas_agendadas += f"{fecha} a las {hora} [datos del paciente: {datos_paciente}]\n"
                        cantidad_citas += 1
                        print(f"Cita agendada con exito para el {fecha} a las {hora}.")

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
                    if cita_a_borrar in citas_agendadas:
                        partes = citas_agendadas.split(cita_a_borrar)
                        if len(partes) == 1:
                            citas_agendadas = partes[0]
                        else:
                             citas_agendadas = partes[0] + partes[1]

                        cantidad_citas = cantidad_citas - 1
                        print(f"Cita del {fecha} a las {hora} cancelada.")
                    else:
                        print("No se encontró esa cita. Por favor, verifique la fecha y hora ingresadas.")
                elif opcion == "4":
                    print("Saliendo del sistema. ¡Gracias por usar el Sistema Clínico, Hasta luego!")
                    exit()
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
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