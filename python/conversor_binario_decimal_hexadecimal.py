"""
Conversor de decimal a binario
             binario a decimal
             decimal a hexadecimal
             hexadecimal a decimal
"""

print("Decimal a binario")


def binarizar(decimal):
    binario=""
    while decimal//2 !=0:
        binario=str(decimal%2)+binario
        decimal=decimal//2
    return str (decimal) + binario
numero=int(input("Introduzca el número que quiere convertir a binario: "))
binario=""
print(binarizar(numero))


print("Binario a decimal")

def decimalizar(binario):
    decimal=""
    numeros=["1","2","4","8","16","32","64","128","256"]
    for i in range (len.numeros):
        binario==numeros+numeros
    return str(decimal) + binario

numero=int(input("Introduzca el número que quiere convertir a binario: "))
decimal=""
print(binarizar(numero))
    
    
    
