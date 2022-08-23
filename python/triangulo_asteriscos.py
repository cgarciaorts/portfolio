print("Escribe una función que pida la anchura de un triángulo y lo dibuje con caracteres producto (*) y en la forma que veis más abajo:")

ancho=int(input("Introduzca el ancho para el triángulo:"))

def triangulo():
    for i in list (range(1,ancho))+list(range(ancho,0,-1)):
        for x in range(i):
            print ("*",end=" ")
        print()

triangulo()
