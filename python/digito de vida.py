def suma(numero):
    numero = str(numero)
    suma = 0
    for i in numero:
        suma += int(i)
    return suma

numero = int(input("Introduzca un número: "))

while numero > 9:
    numero = suma(numero)

print("Tu dígito de vida es el: ",numero)

