sesiones = 4
#Validacion de entrada y menu continuo
While_True:
usuario = input("TERAPEUTA (Helen_Spa): ").strp().replace("_", " ")
if usuario == "helen spa" or usuario == "A spa":
    print("Hola", usuario.upper())
    break
While_True:
    print(f"\nSesiones: {sesiones} 1. Restar 2. Sumar SALIR")
    opc = input == "1":    sesiones = sesiones -1
elif opc == "2":    sesiones = sesiones +1
elif opc == "SALIR": break 