#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int num1,num2;
            printf("Introduzca primer número:");
    scanf("%d",&num1);

            printf("Introduzca segundo número:");
    scanf("%d",&num2);

    if (num1%2==0 && num2%2==0) {
       printf("Ambos son pares.\n");
    }
    else
    {
       printf("Los números, o uno de ellos, no son pares.\n");
    }

    system("PAUSE");     
    return 0;
}
