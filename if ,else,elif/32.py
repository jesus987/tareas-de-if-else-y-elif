def iniciar():
    dulce=raw_input("Elija letra: ")
    if dulce=="a":
        precioProducto=2.5
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)
    elif dulce=="b":
        precioProducto=1.4
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)
    elif dulce=="c":
        precioProducto=4
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)
    elif dulce=="d":
        precioProducto=1.2
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)
def imprimirProductos():
    print "a) chupete : 2.5\nb) gomas : 1.4\nc) caramelo: 4\nd) topline : 1.2"
def calcularVuelto(monto,precioProducto):
    return monto-precioProducto

print imprimirProductos()
monto=input("Ingrese monto: ")
if monto<5:
    print iniciar()
else :
    print "Monto debe ser menor a 5"
