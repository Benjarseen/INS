#Integrantes: Benjamin Rios, Martin Rojas
#Profesor: Rodolfo Aravena
def funcion_factoial(n):
    if n == 0:
        return 1
    retorno = 1
    for i in range(1,n+1,1):
        retorno *= i
    return retorno

def funcion_abosulta(n):
    if n < 0:
        return -1*n
    return n

print("Vamos a calcular el numero de Euler!")
e = 0.0
i = 0
hasta = 0.0001

while(True):
    e+= 1/funcion_factoial(i)
    if(i >= 2 and funcion_abosulta(1/funcion_factoial(i)-1/funcion_factoial(i-1)) < hasta):                                                                                                                                    
        break 
    i+=1 
print("e=",e) 