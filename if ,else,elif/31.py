def numeros(numero):
    if numero==0:
        return "cero"
    elif numero==1:
        return "cero, uno, dos"
    elif numero==2:
        return "cero, uno, dos, tres"
    elif numero==3:
        return "cero, uno, dos, tres, cuatro"
    elif numero==4:
        return "cero, uno, dos, tres, cuatro, cinco"
    elif numero==5:
        return "cero, uno, dos, tres, cuatro, cinco"
    elif numero==6:
        return "cero, uno, dos, tres, cuatro, cinco, seis"
    elif numero==7:
        return "cero, uno, dos, tres, cuatro, cinco, seis, siete"
    elif numero==8:
        return "cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho"
    elif numero==9:
        return "cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve"
    elif numero==10:
        return "cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez"
numero=input("Ingrese numero: ")
if numero>=0 and numero<=10:
    print numeros(numero)
else :
    print "No esta dentro de 0 - 10"
