contador = 0
for i in range(2, 1584):
    for x in range (2,i):
        if i %x == 0:
            break
    else:
        contador +=1
        print("N°",contador,"=", i)
