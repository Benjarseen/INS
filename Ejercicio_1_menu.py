def primos():
    contador = 0
    for i in range(2, 1584):
        for x in range (2,i):
            if i %x == 0:
                break
        else:
            contador +=1
            print("N°",contador,"=", i)
activo = 1
while activo==1:
    print("Bienvenido al programa!\n<<<Menu principal>>>\nOpcion 1: Calcular los primeros 250 numeros primos\nOpcion 2: Salir del programa\n")
    opcion = int(input("Ingrese la opcion: "))
    if opcion ==1:
        print(primos())
        input("\nPresione cualquier tecla para volver al menu")
    if opcion ==2:
        print("Adios!")
        break
    if opcion > 2 or opcion < 1:
        input("\n\nLa opcion ingresada no es valida... presione cualquier tecla para volver al menu:)\n\n")
