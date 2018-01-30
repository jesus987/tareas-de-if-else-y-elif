def _Cuotas(prestamo,meses):
    cuota=prestamo/meses
    return cuota

def _Prestamo():
    prestamo=input("Monto de prestamo: ")
    meses=input("Cuantos meses de pago: ")
    print "Monto de pago por mes: ", _Cuotas(prestamo,meses)

edad=input("Ingrese edad: ")

if edad>=18:
    ingresos=input("Monto de ingresos: ")
    egresos=input("Monto de Egresos")
    if ingresos>egresos:
        _Prestamo()
    else :
        print "Sus ingresos no es mayor que sus egresos"
else :
    print "No es mayor de edad"
