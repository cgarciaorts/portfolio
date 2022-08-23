##Escribir un programa que pida valores y los añada a una lista hasta que el usuario pulse la letra ‘q’.
##Con esa lista introducida por el usuario y haciendo uso de una función, elimine los repetidos en esa lista.
##Luego nos muestre la lista inicialmente y la lista sin los repetidos.
print("Introduce datos, cuando los tengas todos pulse q, tendrás todos los números sin ninguno repetido")
opcion = input('Introduce valor: ')
l= []
l_sin_rep = []
    

    
while(opcion != 'q'):
    l.append(opcion)
    opcion = input('Introduce valor: ')
def lista ():
    for i in l:
        if i not in l_sin_rep:
            l_sin_rep.append(i)

lista()
print("ANTES:", l)
print("DESPUES", l_sin_rep)
