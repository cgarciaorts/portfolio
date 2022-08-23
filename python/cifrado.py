m=input("Introduce el texto a cifrar: ")
alf="abcdefghijklmnñopqrstuvwxyz"
k=int(input("Cuantas letras quieres desplazar el codigo: "))
cifrado="" ##El programa funciona, pero cuando introduzco la funcion NO.
for l in m:
    if l in alf:
        pos_letra = alf.index(l)
        nueva_pos = (pos_letra + k) % len(alf)
        cifrado+= alf[nueva_pos]
    else:
        cifrado+= l

print("Mensaje cifrado:", cifrado)

##def codces(m,alf,k):
##    for l in m:
##        if l in alf:
##            cifrado=""
##            pos_letra = alf.index(l)
##            nueva_pos = (pos_letra + k) % len(alf)
##            cifrado+= alf[nueva_pos]
##        else:
##            cifrado+= l
##    return cifrado
##
##print(codces(m,alf,k))
