##def misplit(strng):##Esta en una lista pero sale letra a letra sin espacios
##    lista=[]
##    espacio=[]
##    for i in strng:
##        if i ==" ":
##            espacio.append(i)
##        else:
##            lista.append(i)
##    return(lista)
##
##def misplit(cadena):##Sale todo junto sin espacios
##    lista=""
##    espacio=""
##    for i in cadena:
##        if i ==" ":
##            espacio+=i
##        else:
##            lista+=i
##    return lista
##
##
##strng="ser o no ser"
##lista=[]
##espacio=[]
##
##for i in strng:
##    while i != " ":
##        lista+=i
##        break
##    else:
##        espacio.append(i)
##
##print(lista)
##
##
##
##
##print(misplit("Ser o no ser, esa es la pregunta"))
##print(misplit("Ser o no ser,esa es la pregunta"))
##print(misplit("   "))
##print(misplit(" abc "))
##print(misplit(""))
