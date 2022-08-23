def ahorcado(fallos,aleatoriacopia):
    if fallos == 1:
        print("        +---+")
        print("        |   |")
        print("        ☺   |")
        print("            |")
        print("            |")
        print("         ___|      ")
    elif fallos == 2:
        print("        +---+")
        print("        |   |")
        print("        ☺   |")
        print("        |   |")
        print("            |")
        print("         ___|      ")
    elif fallos == 3:
        print("        +---+")
        print("        |   |")
        print("        ☺   |")
        print("       /|   |")
        print("            |")
        print("         ___|      ")
    elif fallos == 4:
        print("        +---+")
        print("        |   |")
        print("        ☺   |")
        print("       /|\  |")
        print("            |")
        print("         ___|      ")
    elif fallos == 5:
        print("        +---+")
        print("        |   |")
        print("        ☺   |")
        print("       /|\  |")
        print("       /    |")
        print("         ___|      ")
    elif fallos == 6:
        print("\n\t   --- HA MUERTO ---\n\n")
        print("                           +---+      ")
        print("                           |   |      ")
        print("                           ☺   |     ")
        print("                          /|\  |     ")
        print("                          / \  |     ")
        print("                            ___|      ")
        print("La palabra era:",aleatoriacopia)
        palabra=[]
        letras_usadas=[]
        aleatoria = random.choice(palabras)
        aleatoriacopia = aleatoria
        pal_len = len(aleatoria)
        for x in aleatoria:
            palabra.append("-")
        
def validacion(n1):
    if n1.isdigit():
        val = True
    else:
        val = False
    return val

def acierto(aleatoria,pal_len):
    cont = 0
    for x in aleatoria:
        if x == letra:
            palabra[cont]=letra
        cont+=1

titulo="""
                                                                                      
                                                                                      
    _       _   _     U  ___ u   ____       ____     _      ____      U  ___ u 
U  /"\  u  |'| |'|     \/"_ \/U |  _"\ u U /"___|U  /"\  u |  _"\      \/"_ \/ 
 \/ _ \/  /| |_| |\    | | | | \| |_) |/ \| | u   \/ _ \/ /| | | |     | | | | 
 / ___ \  U|  _  |u.-,_| |_| |  |  _ <    | |/__  / ___ \ U| |_| |\.-,_| |_| | 
/_/   \_\  |_| |_|  \_)-\___/   |_| \_\    \____|/_/   \_\ |____/ u \_)-\___/  
 \\    >>  //   \\       \\     //   \\_  _// \\  \\    >>  |||_         \\    
(__)  (__)(_") ("_)     (__)   (__)  (__)(__)(__)(__)  (__)(__)_)       (__)  \n\n"""
palabra=[]
letras_usadas=[]
palabras=["mesa","silla","coche","libro","cama","halcon","cachimba"]
fallos=0
import random
aleatoria = random.choice(palabras)
aleatoriacopia = aleatoria
pal_len = len(aleatoria)
for x in aleatoria:
    palabra.append("-")
print("------------------------------------------------------------")
rep = "S"
while rep == "S" or rep == "s":
    print()
    print("",titulo)
    print("\t                         +---+")
    print("\t                         |   |")
    print("\t<1> JUGAR                ☺   |")
    print("\t<2> SALIR               /|\  |")
    print("\t                        / \  |")
    print("\t                          ___|")
    print("\n------------------------------------------------------------\n")
    jugar=input("Selecciona una opción: ")
    esdigito = validacion(jugar)
    if esdigito == True:
        jugar = int(jugar)
        if jugar == 1:
            while esdigito == True:
                print("\n------------------------------------------------------------\n")
                print("Palabra >",''.join(palabra))
                print("\n------------------------------------------------------------\n")
                letra=input("Introduce una letra: ")
                esdigito2 = validacion(letra)
                if esdigito2 == False: 
                    if letra in aleatoria:
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)
                        for i in range(1):
                            acierto1 = acierto(aleatoria,pal_len)
                            print("\nLetras usadas:",', '.join(letras_usadas))
                            if "-" not in palabra:
                                print("\n\n\t   ¡¡ ENHORABUENA HAS GANADO !! \n")
                                print("\t                                    ")
                                print("\t                                    ")
                                print("\t                         ☺          ")
                                print("\t                        /|\         ")
                                print("\t                        / \         ")
                                print("\t                                    ")
                                palabra=[]
                                letras_usadas=[]
                                aleatoria = random.choice(palabras)
                                aleatoriacopia = aleatoria
                                pal_len = len(aleatoria)
                                for x in aleatoria:
                                    palabra.append("-")
                                fallos = 0
                                esdigito = False
                    else:
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)
                        print()
                        fallos+=1
                        ahorcadof = ahorcado(fallos,aleatoriacopia)
                        print("\nLetras usadas:",', '.join(letras_usadas))
                        if fallos == 6:
                            aleatoria = random.choice(palabras)
                            aleatoriacopia = aleatoria
                            pal_len = len(aleatoria)
                            for x in aleatoria:
                                palabra.append("-")
                                fallos = 0
                            break
                else:
                    print("\n\t--- ERROR: El valor introducido no es una letra ---")
                    print("\nLetras usadas: ",', '.join(letras_usadas))
    print("\n------------------------------------------------------------\n")
    rep=input("¿Quieres volver al menú?(S/N) ")
    print()
    if rep == "N" or rep == "n":
        rep == "N"
        print("Saliendo del programa......")
        print()
        exit
    print("---------------------------------------------------------------")
