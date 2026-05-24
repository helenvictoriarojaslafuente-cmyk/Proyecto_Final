#Buenas Prácticas:
pacientes = [
    {"nombre": "  JUAN PEREZ  ", "sesiones": 10, "lesion": "Esguince de tobillo grado 2", "terapia": "electrodos y crioterapia", "tiempo": 20},
    {"nombre": "MARIA GOMEZ", "sesiones": 8, "lesion": "Contractura en el cuello", "terapia": "masoterapia y termoterapia", "tiempo": 30},
    {"nombre": "CARLOS LOPEZ", "sesiones": 12, "lesion": "Dolor de rodilla", "terapia": "kinesioterapia pasiva", "tiempo": 45},
    {"nombre": "ANA RODRIGUEZ", "sesiones": 5, "lesion": "Tendinitis", "terapia": "electrodos y kinesioterapia activa", "tiempo": 25},
    {"nombre": "LUIS MARTINEZ", "sesiones": 15, "lesion": "Dolor de espalda bajo", "terapia": "masoterapia y termoterapia", "tiempo": 35}
]

#Bloque de Seguridad Inicial (While):
while True:
    clave = input("Introduce la contraseña: ").strip()
    if clave == "fisio2026":
        print("\n¡Contraseña correcta! Entrando...")
        break
    print("Clave incorrecta. Intenta de nuevo.\n")

#Menú Principal Continuo (While True):
while True:
    print("\n--- GABINETE DE FISIOTERAPIA ---")
    print("1. Lista de pacientes\n2. Modificar sesiones\n3. Ver historial de texto\n4. Salir")

#Control de Errores y Limpieza de Datos (strip, lower, upper):
    opcion = input("Elige una opción: ").strip().lower()
    if opcion in ["1", "uno"]:
        print("\n--- PACIENTES REGISTRADOS ---")
        for i, p in enumerate(pacientes):
            print(f"{i+1}. {p['nombre'].strip()} | {p['lesion']} | {p['terapia']} ({p['tiempo']} min) | Sesiones: {p['sesiones']}")

#Modificación de Variables Numéricas (Sumar/Restar):
    elif opcion in ["2", "dos"]:
        n = int(input("\nNúmero de paciente: ")) - 1
        if 0 <= n < len(pacientes):
            p = pacientes[n]
            print(f"Paciente: {p['nombre'].strip()} ({p['sesiones']} sesiones)")
            accion = input("¿Quieres (A)gregar o (R)estar una sesión?: ").strip().upper()
            
            if accion == "A":
                p["sesiones"] += int(input("¿Cuántas sumamos?: "))
            elif accion == "R" and p["sesiones"] > 0:
                p["sesiones"] -= 1
            print(f"¡Listo! Sesiones actuales: {p['sesiones']}")

#Manipulación de Cadenas de Texto (Comillas triples, replace o slicing):
    elif opcion in ["3", "tres"]:
        n = int(input("\nNúmero de paciente: ")) - 1
        if 0 <= n < len(pacientes):
            p = pacientes[n]
            nombre = p["nombre"].strip()
            
            # Comillas triples
            ficha = """
            ==================================
                    EXPEDIENTE CLÍNICO
            ==================================
            Paciente: {}
            Malestar: {}
            Terapia: {}
            Duración: {} minutos
            ==================================
            """
            # Uso de .replace() y slicing [0:4]
            print(ficha.format(nombre, p["lesion"], p["terapia"].replace(" y ", " + "), p["tiempo"]))
            print(f"Código del archivo: FISIO-{nombre[0:4].upper()}")

    elif opcion in ["4", "salir"]:
        print("\nSaliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida.")