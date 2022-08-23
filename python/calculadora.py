print("                 _                  _               _                        ")
print("                | |                | |             | |                       ")
print("   ___    __ _  | |   ___   _   _  | |   __ _    __| |   ___    _ __    __ _ ")
print("  / __|  / _` | | |  / __| | | | | | |  / _` |  / _` |  / _ \  | '__|  / _` |")
print(" | (__  | (_| | | | | (__  | |_| | | | | (_| | | (_| | | (_) | | |    | (_| |")
print("  \___|  \__,_| |_|  \___|  \__,_| |_|  \__,_|  \__,_|  \___/  |_|     \__,_|\n\n")
 
print ("                              1. Suma")
print ("                              2. Resta")
print ("                              3. Multiplicacion")
print ("                              4. Division")
print ("                              5. Division Entera")
print ("                              6. Resto")
print ("                              7. Raíz cuadrada (Introduzca el mismo número dos veces)")
print ("                              8. Potencia (El primer numero será la base y el 2º el exponente)")

opcion=int(input("Introduzca el número de la opción que desee: "))

num1=int(input("Introduzca un número: "))
num2=int(input("Introduzca un número: "))
#1
def suma(num1,num2):
    suma=num1+num2
    return suma

suma_total=suma(num1,num2)
#2
def resta(num1,num2):
    resta=num1-num2
    return resta

resta_total=resta(num1,num2)
#3
def multiplicacion(num1,num2):
    multiplicacion=num1*num2
    return multiplicacion

multiplicacion_total=multiplicacion(num1,num2)
#4
def division (num1,num2):
    cociente=num1/num2
    return cociente

division_total=division(num1,num2)
#5
def division_entera(num1,num2):
    cociente=num1//num2
    return cociente

cociente_entero=division_entera(num1,num2)
#6
def resto (num1,num2):
    resto=num1%num2
    return resto

resto_total=resto(num1,num2)
#7
def raiz(num1):
    raiz=num1**0.5
    return raiz

raiz_total=raiz(num1)
#8
def potencia(num1,num2):
    potencia=num1**num2
    return potencia

potencia_total=potencia(num1,num2)

def salir(opcion):
    if opcion > 8:
	    print("Introduzca una opción válida")
    return opcion
salida=salir(opcion)




while opcion > 0 and opcion <9:
	
    if opcion == 1:
        suma
        print("El resultado es: ",suma_total)
        break

    elif opcion == 2:
        resta
        print("El resultado es: ",resta_total)
        break

    elif opcion == 3:
        multiplicacion
        print("El resultado es: ",multiplicacion_total)
        break

    elif opcion == 4:
        division
        print("El resultado es: ",division_total)
        break

    elif opcion == 5:
        division_entera
        print("El resultado es: ",cociente_entero)
        break

    elif opcion == 6:
        resto
        print("El resultado es: ",resto_total)
        break

    elif opcion == 7:
        raiz
        print("El resultado es: ",raiz_total)
        break

    elif opcion == 8:
        potencia
        print("El resultado es: ",potencia_total)
        break

    else:
	    salida
        
