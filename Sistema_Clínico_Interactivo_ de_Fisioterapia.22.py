# Fisiterapia
print("==================================================")
print("        SISTEMA INTERACTIVO DE FISIOTERAPIA        ")
print("==================================================\n")

usuarios = {}
Login = False
citas = []
usuario_actual = ""

# True significa que el tratamiento está LIBRE. False significa OCUPADO.
tratamientos_libres = {
    "1": True,
    "2": True,
    "3": True
}

while not Login:
    print("""Por favor Selecciona una Opción:
    1. Iniciar Sesión
    2. Registrarse
    3. Salir del sistema\n""")
    
    opcion = input("Ingrese el número de la opción que desea: ").strip()  

    if opcion == "1":
        while True:
            nombre = input("Ingrese su nombre de usuario: ").strip().title()
            if nombre.isalpha():
                break
            else:
                print("No se admiten números en los nombres.")

        # CONTRASEÑA
        while True:    
            contraseña = input("Ingrese su contraseña: ").strip()
            if len(contraseña) != 4: 
                print("Solo se admiten exactamente 4 caracteres.")
            else:
                if contraseña in usuarios and usuarios[contraseña] == nombre:
                    print("\n==================================================")
                    print("¡Inicio de sesión exitoso! Bienvenid@, ", nombre)
                    print("==================================================")
                    Login = True
                    usuario_actual = nombre
                    break
                else:
                    print("Los datos no coinciden o no existe la cuenta")
                    break              
                    
    # NUEVO
    elif opcion == "2":
        while True:
            print("\n--- Registrarse ---")
            nuevo_usuario = input("Ingrese un nombre de usuario para registrarse: ").strip().title()
            if nuevo_usuario.isalpha():
                break
            else:
                print("No se admiten números en los nombres.")
                
        while True:       
            nueva_contraseña = input("Ingrese una contraseña para registrarse: ").strip()            
            if len(nueva_contraseña) != 4:
                print("Solo se admiten 4 caracteres.")
            else:
                usuarios[nueva_contraseña] = nuevo_usuario
                print("\n==================================================")
                print("Registro con éxito: ", nuevo_usuario)
                print("Ahora puede iniciar sesion.")
                print("==================================================")
                break
                
    # ======================SALIR======================    
    elif opcion == "3":
        print("Gracias por visitarnos, vuelva pronto.")
        break  
        
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.") 

# ==================================================
# SESIÓN INICIADA
# ==================================================
while Login:
    print("""\nMenú Principal del Sistema Clínico
     1. Agendar Cita
     2. Cancelar Cita
     3. Ver Citas Agendadas
     4. Salir (Cerrar Sesión)\n""") 
    opcion = input("Ingrese el número de la opción que desea: ").strip()
    
    # ====================== Agendar Citas ====================== 
    if opcion == "1":
        while True:
            print("\n========  Agendar Cita  ========\n")
            print("Tratamientos Disponibles:")
            
            # Revisamos el estado de cada tratamiento para guardarlo en texto
            if tratamientos_libres["1"]:
                est_1 = "Disponible"
            else:
                est_1 = "OCUPADO"
                
            if tratamientos_libres["2"]:
                est_2 = "Disponible"
            else:
                est_2 = "OCUPADO"
                
            if tratamientos_libres["3"]:
                est_3 = "Disponible"
            else:
                est_3 = "OCUPADO"
            
            # Imprimimos el menú usando comas de forma sencilla
            print("1. Fisioterapia Deportiva (", est_1, ")")
            print("2. Rehabilitación Postoperatoria (", est_2, ")")
            print("3. Terapia de Relajación y Descarga (", est_3, ")")
            print("4. Volver al menú.\n")
         
            tratam_opcion = input("Seleccione el número del tratamiento o volver al menú: ").strip()
            
            if tratam_opcion == "1":
                if not tratamientos_libres["1"]:
                    print("\nLa Fisioterapia Deportiva ya se encuentra agendada.")
                    continue
                else:
                    tratamiento = "Fisioterapia Deportiva"
                    precio_base = "Bs. 120"
            elif tratam_opcion == "2":
                if not tratamientos_libres["2"]:
                    print("\nLa Rehabilitación Postoperatoria ya se encuentra agendada.")
                    continue
                else:
                    tratamiento = "Rehabilitación Postoperatoria"
                    precio_base = " Bs. 150"
            elif tratam_opcion == "3":
                if not tratamientos_libres["3"]:
                    print("\nLa Terapia de Relajación ya se encuentra agendada.")
                    continue
                else:
                    tratamiento = "Terapia de Relajación y Descarga"
                    precio_base = "Bs. 150"
            elif tratam_opcion == "4":
                print("Volviendo al menú.")
                break
            else:
                print("Opción no válida. Debe escoger entre 1-4.")
                continue
            
            # Validación de Fecha Real
            while True:
                fecha = input("Ingrese la fecha (Formato DD/MM, ej: 15/08): ").strip()

                if len(fecha) == 5 and fecha[2] == "/":
                    partes = fecha.split("/")
                    dia_texto = partes[0]
                    mes_texto = partes[1]
                    
                    if dia_texto.isdigit() and mes_texto.isdigit():
                        dia = int(dia_texto)
                        mes = int(mes_texto)
                        
                        if mes >= 1 and mes <= 12:
                            if dia >= 1 and dia <= 31:
                                break  
                            else:
                                print("Día inválido. Debe ser entre 01 y 31.")
                        else:
                            print("Mes inválido. Debe ser entre 01 y 12.")
                    else:
                        print("La fecha solo debe contener números separados por '/'.")
                else:
                    print("Formato incorrecto. Use exactamente DD/MM (23/11).")

            # Validación de Hora Real
            while True:
                hora = input("Ingrese la hora (Formato HH:MM, ej: 14:30): ").strip()
                
                if len(hora) == 5 and hora[2] == ":":
                    partes_hora = hora.split(":")
                    hh_texto = partes_hora[0]
                    mm_texto = partes_hora[1]
                    
                    if hh_texto.isdigit() and mm_texto.isdigit():
                        hh = int(hh_texto)
                        mm = int(mm_texto)        
                        if hh >= 8 and hh <= 17:
                            if mm >= 0 and mm <= 59:
                                print("\n¡Cita correctamente agendada para la fecha:", fecha, "y hora:", hora, ", para el paciente", usuario_actual, "! Gracias por agendar.")

                                # Guardamos la cita usando sumas de texto (+). Al final dejamos el número de opción pegado.
                                nueva_cita = "Tratamiento: " + tratamiento + "  Fecha: " + fecha + "  Hora: " + hora + "  ID:" + tratam_opcion
                                citas.append(nueva_cita)           
                                # Bloqueamos el tratamiento elegido cambiándolo a False
                                tratamientos_libres[tratam_opcion] = False

                                # Formato de precios usando .replace()
                                precio_local = precio_base.replace (",", ".")
                                # Impresión del ticket digital con formato usando comas para separar cada línea
                                print("\n==================================================")
                                print("            TICKET DIGITAL: FISIOTERAPIA            ")
                                print("====================================================")
                                print(f" PACIENTE:    {usuario_actual}")
                                print(f" TRATAMIENTO: {tratamiento}")
                                print(f" FECHA:       {fecha}")
                                print(f" HORA:        {hora}")
                                print(f" PRECIO:      {precio_local}")
                                print("====================================================")
                                break  
                             
                            else:
                                print("Minutos inválidos. Debe ser entre 00 y 59.")
                        else:
                            print("Hora inválida. Debe ser entre 08 y 17.")
                    else:
                        print("La hora solo debe contener números separados por ':'.")
                else:
                    print("Formato incorrecto. Use exactamente HH:MM de 24 horas (08:15).")
            
            break 

    # ====================== Cancelar Citas ====================== 
    elif opcion == "2":
        print("\n========  Cancelar Cita  ========")
        if len(citas) == 0:
            print("No tienes ninguna cita registrada para cancelar.")
        else:
            # NUEVO: Mostramos la lista usando un bucle 'while' básico en vez de 'for'
            contador = 0
            while contador < len(citas):
                print(contador + 1, ".", citas[contador])
                contador = contador + 1
                
            num = input("\nIngrese el número de la cita que desea cancelar: ").strip()
            if num.isdigit():
                indice = int(num) - 1
                if indice >= 0 and indice < len(citas):
                    # Guardamos temporalmente el texto de la cita para poder liberar el ID antes de borrarla
                    cita_a_borrar = citas[indice]
                    id_tratamiento = cita_a_borrar[-1] 
                    
                    # NUEVO: Usamos 'del' en vez de '.pop()' para borrar el elemento de la lista
                    del citas[indice]
                    
                    # Volvemos a liberar el espacio poniéndolo en True
                    tratamientos_libres[id_tratamiento] = True
                    
                    print("¡Cita cancelada y tratamiento liberado con éxito!")
                else:
                    print("Ese número de cita no existe.")
            else:
                print("Por favor, ingrese un número válido.")

    # ====================== Ver Citas Agendadas ====================== 
    elif opcion == "3":
        print("\n========  Citas Agendadas  ========")
        if len(citas) == 0:
            print("No hay ninguna cita registrada en este momento.")
        else:
            # NUEVO: Mostramos las citas usando un bucle 'while' básico en vez de 'for'
            contador = 0
            while contador < len(citas):
                print(contador + 1, ".", citas[contador])
                contador = contador + 1

    # ====================== Salir ====================== 
    elif opcion == "4":
        print("Cerrando sesión de ", usuario_actual, "... Hasta luego.")
        Login = False