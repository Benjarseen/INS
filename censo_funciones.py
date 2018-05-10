def censo():
    ###Definimos las variables que se nos pide recopilar e imprimir (a usar con contadores)###
    cantidad_personas = 0
    cantidad_mujeres = 0
    cantidad_hombres = 0
    cantidad_mprof = 0
    #############################
    viviendas = int(input("¿Cuantas viviendas va a censar?: ")) ###Preguntamos al usuario viviendas a censar###
    for i in range(1, viviendas+1): ###Definimos el rango desde el valor minimo que podria adquirir hasta el numero de viviendas elegidas por el usuario sumandole 1(Esto debido a que los range no toman el ultimo valor del rango)###
        print("Viviendas a censar: ", i)
        personas = int(input("¿Cuantas personas hay en la vivienda?: "))
        cantidad_personas = cantidad_personas + personas ###contador de cantidad de personas###
        for i in range(1, personas+1):
            print("Ingrese los datos de la persona") ###Le pedimos al usuario ingresar los datos correspondientes###
            nombre = input("Nombre: ")
            genero = input("Genero: ")
            edad = input("Edad: ")
            nivel_estudio = input("Nivel de estudio(B = Basico, M = Medio, S = Superior): ")
            comuna = input("Comuna: ")
            
            if nivel_estudio == "S" and genero == "f":
                cantidad_mprof = cantidad_mprof+1 ###Contador de mujeres y además profesionales###
            if genero == "f": 
                cantidad_mujeres = cantidad_mujeres+1 ###Contador de mujeres###
            if genero == "m":
                cantidad_hombres = cantidad_hombres+1 ###Contador de Hombres###
###Imprimimos los datos recopilados###
    print("Cantidad de personas censadas: ",cantidad_personas)
    print("Cantidad de hombres censados: ",cantidad_hombres)
    print("Cantidad de mujeres censados: ",cantidad_mujeres)
    print("Cantidad de mujeres profesionales censadas: ",cantidad_mprof)
censo()###llamamos a la funcion###                