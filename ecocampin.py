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
    else:
        print("opcion fuera de rango")
        