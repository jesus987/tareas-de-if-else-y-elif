def sumar(num1, num2):
    return num1+num2
def restar(num1, num2):
    return num1-num2
def multiplicar(num1, num2):
    return num1*num2
def dividir(num1, num2):
    return num1/num2
def calcular(x, y, z):
    resultado=dividir(multiplicar(sumar(x,y),restar(y,z)),sumar(x**2,y**2))**2
    return resultado

x=input("Ingrese x: ")
x=x*1.0
y=input("Ingrese y: ")
y=y*1.0
z=input("Ingrese z: ")
z=z*1.0
print calcular(x,y,z)
