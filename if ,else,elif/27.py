ef valorAbsoluto(numero):
    if numero%3==0 and numero%7==0:
    if numero<0:
        return numero*-1
    elif numero>=0:
        return numero
    else :
        return "No es multiplo de 3 y 7"
numero=input("Ingrese numero: ")
