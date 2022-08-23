alf = "abcdefghijklmnñopqrstuvwxyz"
mensaje = input("Escribe un mensaje: ")
num = int(input("Escribe cuantas posiciones la quieres mover: "))
#funcion comprueba que la letra esta en la lista, recorre la lista para encontrar la posicion , luego a la posicion le sumamos los numeros que las queremos mover,comprobamos que el numero no es mayor que el string y si lo es hacemos una resta y ponemos la posicion
def desplazar(letra,alf,num):
    contador = 0
    if letra in alf: 
            for i in alf:
                contador+= 1
                if i == letra:
                    posicion = (contador + num)-1
                    if posicion >= len(alf):
                        posicionMovida = posicion - len(alf)
                        print(alf[posicionMovida], end="")
                        
                    else:
                        print(alf[posicion],end="")
                        
                        
    if letra == " ":
        print(" ",end="")
    

#dar la vuelta al string            
def alfnv(alf):
    posicionreverse = 0
    for i in range(len(alf)):
        posicionreverse-=1
    
    return posicionreverse

#esta funcion coge el mensaje escrito por pantalla y lo pasa por la funcion desplazar para asi codificarla
def codificar(mensaje,alf,num):
    for letra in mensaje:
        desplazar(letra,alf,num)
        

#codigo
codificar(mensaje,alf,num)
