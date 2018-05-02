#Ayudiantia checkear primos solo con while
#Primos con porcentaje de proceso para listas muy largas
#Usando un ouput para mejorar el rendimiento (1millon checkeos en menos de 40 segs [en mi PC])

n=2 #Partir del 2 ya que 1 no se considera primo
output = "" #El output

show = int(input("Ingrese numeros a checkear: ")) #obtener tamano de lista


while n<=show:
    isPrime = True #Auxiliar para ver si es primo
    k = 2 #iniciamos en 2 el checkeo ya que si se inicia de 1 ninguno seria primo (en programacion)
    stop = False #Auxiliar para detener el while (no nos han ensenado break)
    sqrt = int(n**(1/2)) #Raiz cuadrada para mejor rendimiento, no calculado directamente en while para mejor rendimiento
    #es preciso recordar que no vale la pena verificar resto de numeros mas grandes ya que no son parte de su divisor

    
    if n%2 == 0 and n > 2: #no usar pares mas rendimiento
        stop = False
        
    while k <= sqrt and not stop: #Todo lo que tiene que ver con primos
        if n%k == 0:
            isPrime = False
            stop = True
        k += 1
        
    if isPrime: #Si es primo agregamos al output
        output += str(n)+"\n" #str() para pasar entero a cadena, no se puede sumar un numero a una cadena!!!

    p = 100*n/show #porcentaje de proceso
    if p%1 == 0: #Solo mostrar porcentaje entero
        print(int(p),"% Del proceso") #mostramos procentaje, damos int(p) para no mostrar el punto flotante
    n+=1
print("Imprimiendo....") #Si se elije uno grande se demora el output, por lo tanto mensaje
print(output) #output
1571