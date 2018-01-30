#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int num1,num2;
            printf("Introduzca número del 1 al 5:");
    scanf("%d",&num1);

            printf("Introduzca número del 1 al 5:");
    scanf("%d",&num2);

    if (num1!=4 && num2!=4) {
       printf("Ambos son primos.\n");
    }
    else
    {
       printf("Los números, o uno de ellos, no son primos.\n");
    }

    system("PAUSE");     
    return 0;
}
