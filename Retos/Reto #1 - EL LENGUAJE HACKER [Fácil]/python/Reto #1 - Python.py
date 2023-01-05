'''*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 '''

texto = input ("Introduce un texto: ")


for caracter in texto :
    if caracter.lower() == "a" :
        print ("4", end="")
    elif caracter.lower == "b" :
        print ("I3", end="")
    elif caracter.lower() == "c" :
        print ("[", end="")
    elif caracter.lower() == "d" :
        print (")", end="")
    elif caracter.lower() == "e" :
        print ("3", end="")
    elif caracter.lower() == "f" :
        print ("|=", end="")
    elif caracter.lower() == "g" :
        print ("&", end="")
    elif caracter.lower() == "h" :
        print ("#", end="")
    elif caracter.lower() == "i" :
        print ("1", end="")
    elif caracter.lower() == " " :
        print (" ", end="")
    elif caracter.lower() == "j" :
        print (",_|", end="")
    elif caracter.lower() == "k" :
        print (">|", end="")
    elif caracter.lower() == "l" :
        print ("1", end="")
    elif caracter.lower() == "m" :
        print ("'/\/\'", end="")
    elif caracter.lower() == "n" :
        print ("^/", end="")
    elif caracter.lower() == "o" :
        print ("0", end="")
    elif caracter.lower() == "p" :
        print ("|*", end="")
    elif caracter.lower() == "q" :
        print ("(_,)", end="")
    elif caracter.lower() == "r" :
        print ("I2", end="")
    elif caracter.lower() == "s" :
        print ("5", end="")
    elif caracter.lower() == "t" :
        print ("7", end="")
    elif caracter.lower() == "u" :
        print ("(_)", end="")
    elif caracter.lower() == "v" :
        print ("\/", end="")
    elif caracter.lower() == "w" :
        print ("\/\/", end="")
    elif caracter.lower() == "x" :
        print ("><", end="")
    elif caracter.lower() == "y" :
        print ("j", end="")
    elif caracter.lower() == "z" :
        print ("2", end="")
    elif caracter == "1" :
        print ("(L", end="")
    elif caracter == "2" :
        print ("R", end="")
    elif caracter == "3" :
        print ("E", end="")
    elif caracter == "4" :
        print ("A", end="")
    elif caracter == "5" :
        print ("S", end="")
    elif caracter == "6" :
        print ("b", end="")
    elif caracter == "7" :
        print ("T", end="")
    elif caracter == "8" :
        print ("B", end="")
    elif caracter == "9" :
        print ("g", end="")
    elif caracter == "0" :
        print ("o", end="")
    

    


