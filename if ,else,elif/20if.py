#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int num1,num2,num3;
           
            printf("Introduzca número 1:");
    scanf("%d",&num1);
   
    printf("Introduzca número 2:");
    scanf("%d",&num2);

    printf("Introduzca número 3:");
    scanf("%d",&num3);

    if (num1%num2==num3)
    {
         printf("El tercer número es el resto de la división de los dos primeros.\n");
    }
    else
    {
         printf("El tercer número NO es el resto de la división de los dos primeros.\n");       
    }

    system("PAUSE");     
    return 0;
}
