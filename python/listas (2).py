print("Escribe un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.")
num=int(input("Dígame cuántas palabras tiene la lista: "))

if num < 1:
    print("Introduzca un número válido.")
    
else:
    lista = []
    for i in range(num):
        palabra=input("Dígame la palabra: ")
        lista += [palabra]
    print("La lista creada es:", lista)

    num2 = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))

    if num2 < 1:
        print("¡Imposible!")
    else:
        eliminar = []
        for i in range(num2):
            palabra=input("Dígame la palabra:")
            eliminar += [palabra]
        print("La lista de palabras a eliminar es:", eliminar)
        for i in eliminar:
            for j in range(len(lista)-1,-1,-1):
                if lista[j] == i:
                    del(lista[j])
        print("La lista es ahora:",lista)
