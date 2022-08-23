palabra=input("Introduce una palabra: ")
palabra2="nabucodonosorfgh"
suma=""

for i in palabra:
    
    if i in palabra2:
        suma+=str(i)
        
        if palabra==suma:
            print("La palabra está en la cadena")

    else:
        print("No está la palabra")
        break
