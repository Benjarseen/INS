activo = 1
mi_lista = []
print("Bienvenido al programa!\n")
while activo ==1:
    aleatorio = input("\nIngrese cualquier palabra: ")
    mi_lista.append(aleatorio)
    if aleatorio =="fin":
        mi_lista.remove("fin")
        print("\n\nLas palabras escritas fueron: ",mi_lista)
        break
    if aleatorio == aleatorio:
        print("\n\n>>>Para finalizar solo escribe ´fin´<<<")
        aleatorio1 = input("Ingrese otra palabra: ")
        mi_lista.append(aleatorio1)
    if aleatorio1 =="fin":
        mi_lista.remove("fin")
        print("\n\nLas palabras escritas fueron: ",mi_lista)
        break
    

