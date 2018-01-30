def xmayor(num1,num2):
    if num1%num2==0:
        print num1," es multipli de ", num2
    else:
        print num1," no es multiplo de ", num2
num1=input("Primer Numero: ")
num2=input("Segundo numero:")
print xmayor(num1,num2)
