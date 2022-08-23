print("Escribe una función que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):")
anchura=int(input("Introduzca la anchura del rectángulo: "))
altura=int(input("Introduzca la altura del rectángulo: "))

for i in range(anchura):
    print("* ", end="")
print()

for i in range(altura - 2):
    print("* ", end="")
    for j in range(anchura - 2):
        print("  ", end="")
    print("*")

for i in range(anchura):
    print("* ", end="")
