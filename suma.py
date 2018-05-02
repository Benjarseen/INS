print("Bienvenido al programa!\n","Vamos a realizar una suma!")
num1 = input("\nIngrese el primer termino: ")
num2 = input("\nIngrese el segundo termino: ")
resultado = int(num1) + int(num2)
if (resultado < 5):
    print("\nLa suma es menor a 5","\nEl resultado es: ", resultado)
elif (resultado > 5):
    print("\nLa suma es mayor que 5","\nEl resultado es: ", resultado)
elif (resultado ==5):
    print("\nLa suma es igual a 5","\nEl resultado es: ", resultado)
    