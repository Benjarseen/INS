""""n = int(input("Ingrese un numero entero positivo: "))
if n > 0:
    for i in range(2, n):
        
        creciente = 2
        
        esPrimo = True
        
        while esPrimo and creciente < i:
            
            if i % creciente==0:
                
                esPrimo= False
            
            else:
            
                creciente +=1
        if esPrimo:
            print(i, "Es primo")
else:
    print("El numero ingresado no es valido. ")"""""
n = int(input)
contador = 0

for i in range(2, n):
    if i%n ==1:
        contador +=1
        print(contador, i, "es primo")
        
print(i)
