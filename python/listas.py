print("Escribe un programa que pida cuántas listas de palabras se quieren crear y a continuación solicite el número de palabras que tiene la lista, para después pedir la introducción de esas palabras. Una vez hecho, deberéis crear una lista, en la que cada elemento de la lista sea cada una de las listas creadas anteriormente.")
numero_listas=int(input("Introduzca el número de listas desea crear: "))
lista=[]
lista_completa=[]

for i in range (numero_listas):
    numero_palabra=int(input("Introduzca el número de palabras: "))
    lista=[]
    for j in range (numero_palabra):
        palabra=input("Introduzca la palabra: ")
        lista.append(palabra)
        print(lista)
    lista_completa.append(lista)

print(lista_completa)
