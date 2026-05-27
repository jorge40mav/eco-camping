print("gestion eco campingbosque vivo")
capacidad_maxima = 15 
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\=====menu de control de registro===")
    print("1. ver sitios disponobles")
    print("2. registro de vehiculos en el sistema(entrada)")
    print("3. registro de salida de vehiculos (salida)")
    print("4. estado actual del camping")
    print("5 salir")
    try:
        opcion = int(input("seleccione una opcion (1-5):"))
    except ValueError:
        print("opcion no valida , por favor seleccione entre 1 y 5") 
        continue
    #Despegue de opciones
    if opcion == 1:
        disponible = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO]sitios libres para recibir vehiculos: {disponible}")
    elif opcion == 2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if sitios_libres == 0
           print("lo sentimos mo queda espacios en el camping")
        else:
            try:
                ingreso = int(input("cuantos"))
                if ingreso <= 0:
                    print("Error:la cantidad de ingreso debe debe ser mayor a 0")
                elif ingreso > sitios_libres:
                    print(f"solo puede ingresar un maximo de {sitios_libres}sitios")
                else:
                    sitios_ocupados += ingreso
                    print(f"ingresos registrado se han ocupado{ingreso} de sitios")
            except ValueError:
                print("Error: debe ingresar un numero valido")
    else:
        print("opcion fuera de rango")
