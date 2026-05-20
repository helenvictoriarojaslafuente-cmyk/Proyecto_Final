# ==========================================
# REQUISITO 6: BUENAS PRÁCTICAS (COMENTARIOS)
# Proyecto: Sistema Clínico Interactivo de Fisioterapia
# ==========================================

print("=== INICIALIZANDO SISTEMA DE FISIOTERAPIA ===")

# --- BASE DE DATOS CLÍNICA (10 PACIENTES ORIGINALES) ---
# Requisito 4: Estados iniciales numéricos (sesiones) que se van a modificar en el menú
pacientes = [
    {"nombre": "  JUAN PEREZ  ", "sesiones": 10, "lesion": "Esguince de tobillo grado 2", "terapia": "electrodos y crioterapia", "tiempo": 20},
    {"nombre": "MARIA GOMEZ", "sesiones": 8, "lesion": "Contractura cervical crónica", "terapia": "masoterapia y termoterapia", "tiempo": 30},
    {"nombre": "CARLOS LOPEZ", "sesiones": 12, "lesion": "Post-operatorio de LCA", "terapia": "kinesioterapia pasiva", "tiempo": 45},
    {"nombre": "ANA RODRIGUEZ", "sesiones": 5, "lesion": "Tendinitis aquilea", "terapia": "electrodos y kinesioterapia activa", "tiempo": 25},
    {"nombre": "LUIS MARTINEZ", "sesiones": 15, "lesion": "Lumbalgia mecanopostural", "terapia": "masoterapia y termoterapia", "tiempo": 35},
    {"nombre": "ELENA DIAZ", "sesiones": 6, "lesion": "Fractura de radio consolidada", "terapia": "kinesioterapia pasiva y crioterapia", "tiempo": 40},
    {"nombre": "PEDRO SANCHEZ", "sesiones": 20, "lesion": "Desgarro muscular en isquiotibiales", "terapia": "electrodos, masoterapia y kinesioterapia activa", "tiempo": 30},
    {"nombre": "LAURA FERNANDEZ", "sesiones": 4, "lesion": "Fascitis plantar aguda", "terapia": "termoterapia y crioterapia", "tiempo": 15},
    {"nombre": "JORGE RAMIREZ", "sesiones": 7, "lesion": "Bursitis subacromial", "terapia": "kinesioterapia pasiva y masoterapia", "tiempo": 40},
    {"nombre": "SOFIA TORRES", "sesiones": 11, "lesion": "Artrosis de rodilla", "terapia": "electrodos y crioterapia", "tiempo": 25}
]

# ==========================================
# REQUISITO 1: BLOQUEO DE SEGURIDAD INICIAL (while)
# ==========================================
contrasena_correcta = "fisio2026"
acceso_concedido = False

while not acceso_concedido:
    # Requisito 3: Limpieza con .strip() en el login para evitar fallas por espacios
    intento_clave = input("Ingrese la contraseña del gabinete: ").strip()
    
    if intento_clave == contrasena_correcta:
        print("\n¡Acceso concedido al sistema clínico!")
        acceso_concedido = True
    else:
        print("Contraseña incorrecta. Intente de nuevo.\n")

# ==========================================
# REQUISITO 2: MENÚ PRINCIPAL CONTINUO (while True)
# ==========================================
while True:
    print("\n" + "="*55)
    print("      GABINETE DE FISIOTERAPIA - PANEL DE CONTROL")
    print("="*55)
    print("1. Ver lista de pacientes, lesiones y terapias")
    print("2. Modificar sesiones de un paciente (Numérico)")
    print("3. Generar expediente clínico detallado (Texto)")
    print("4. SALIR")
    print("="*55)
    
    # Requisito 3: Control de errores con .strip() y .lower() al recibir la opción
    opcion = input("Seleccione una opción (1-4): ").strip().lower()
    
    # --- OPCIÓN 1: MOSTRAR LOS PACIENTES Y SUS DIAGNÓSTICOS ---
    if opcion == "1" or opcion == "uno":
        print("\n--- LISTADO GENERAL DE PACIENTES ---")
        for i, p in enumerate(pacientes):
            # Limpiamos visualmente los nombres al mostrarlos en el menú usando .strip()
            print(f"[{i+1}] {p['nombre'].strip()}")
            print(f"    Lesión: {p['lesion']} | Terapia: {p['terapia']} ({p['tiempo']} min) | Sesiones: {p['sesiones']}")
            print("-" * 55)

    # --- OPCIÓN 2: MODIFICACIÓN DE VARIABLES NUMÉRICAS (SUMAR/RESTAR) ---
    elif opcion == "2" or opcion == "dos":
        print("\n--- MODIFICAR SESIONES DE TRATAMIENTO ---")
        for i, p in enumerate(pacientes):
            print(f"{i+1}. {p['nombre'].strip()} ({p['sesiones']} sesiones restantes)")
            
        idx = int(input("\nSeleccione el número de paciente a modificar: ")) - 1
        
        if 0 <= idx < len(pacientes):
            p_sel = pacientes[idx]
            print(f"\nPaciente: {p_sel['nombre'].strip()}")
            print("A. Agregar sesiones al tratamiento (Sumar)")
            print("B. Descontar sesión por asistencia (Restar)")
            
            sub_opcion = input("Elija (A/B): ").strip().upper() # Requisito 3: .upper()
            
            # Requisito 4: Sumar o restar valores cuantitativos a un estado numérico
            if sub_opcion == "A":
                cantidad = int(input("¿Cuántas sesiones desea añadir?: "))
                p_sel["sesiones"] += cantidad
                print(f"¡Actualizado! Total de sesiones actuales: {p_sel['sesiones']}")
            elif sub_opcion == "B":
                if p_sel["sesiones"] > 0:
                    p_sel["sesiones"] -= 1
                    print(f"¡Sesión descontada con éxito! Le quedan: {p_sel['sesiones']} sesiones.")
                else:
                    print("Atención: El paciente ya no cuenta con sesiones disponibles.")
            else:
                print("Opción inválida.")
        else:
            print("El número de paciente seleccionado no existe.")

    # --- OPCIÓN 3: MANIPULACIÓN DE CADENAS DE TEXTO ---
    elif opcion == "3" or opcion == "tres":
        print("\n--- EXPEDIENTE DIGITAL Y FORMATEO DE TEXTO ---")
        for i, p in enumerate(pacientes):
            print(f"{i+1}. {p['nombre'].strip()}")
            
        idx = int(input("\nSeleccione el paciente para generar reporte: ")) - 1
        
        if 0 <= idx < len(pacientes):
            p = pacientes[idx]
            
            # Requisito 5a: Comillas triples para estructurar un reporte del negocio limpio
            reporte_plantilla = """
            +--------------------------------------------------------+

            |               HISTORIAL CLÍNICO DIGITAL                |
            +--------------------------------------------------------+

            | PACIENTE: {0}
            | DIAGNÓSTICO: {1}
            | TERAPIA DESIGNADA: {2}
            | TIEMPO DE SESIÓN: {3} minutos
            +--------------------------------------------------------+
            """
            
            # Requisito 5b: Limpieza inicial del string
            nombre_limpio = p["nombre"].strip()
            
            # Requisito 5b: Slicing (posiciones) para generar un ID clínico usando las primeras 4 letras
            id_clinico = nombre_limpio[0:4].upper()
            
            # Requisito 5b: .replace() para estandarizar los datos del negocio (ej. cambiar la palabra 'y' por un conector visual)
            terapia_formateada = p["terapia"].replace(" y ", " + ")
            
            # Imprimimos el reporte final aplicando las herramientas de texto y formateo
            print(reporte_plantilla.format(nombre_limpio, p["lesion"], terapia_formateada, p["tiempo"]))
            print(f"Código Único de Ficha (Slicing): EXP-{id_clinico}")
        else:
            print("Selección incorrecta.")

    # --- OPCIÓN 4: SALIR EXPLICÍTAMENTE ---
    elif opcion == "4" or opcion == "salir": # Requisito 2 y 3: Valida "SALIR" gracias a la limpieza previa
        print("\nCerrando sistema interactivo de consola. ¡Gabinete fuera de línea!")
        break
        
    else:
        print("\nOpción no válida. Por favor, intente de nuevo de acuerdo al menú.")