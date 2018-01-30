#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,mayor,menor;
           
            mayor=0;
            menor=10;
           
            printf("Introduzca número 1:");
    scanf("%d",&num1);

    if (num1>mayor)
    {
       mayor=num1;
    }
    else if (num1<menor)
    {
       menor=num1;
    }

            printf("Introduzca número 2:");
    scanf("%d",&num2);

    if (num2>mayor)
    {
       mayor=num2;
    }
    else if (num2<menor)
    {
       menor=num2;
    }
   
    printf("Introduzca número 3:");
    scanf("%d",&num3);

    if (num3>mayor)
    {
       mayor=num3;
    }
    else if (num3<menor)
    {
       menor=num3;
    }
   
    printf("Introduzca número 4:");
    scanf("%d",&num4);

    if (num4>mayor)
    {
       mayor=num4;
    }
    else if (num4<menor)
    {
       menor=num4;
    }

    printf("Introduzca número 5:");
    scanf("%d",&num5);

    if (num5>mayor)
    {
       mayor=num5;
    }
    else if (num5<menor)
    {
       menor=num5;
    }
   
    printf("Introduzca número 6:");
    scanf("%d",&num6);

    if (num6>mayor)
    {
       mayor=num6;
    }
    else if (num6<menor)
    {
       menor=num6;
    }
   
    printf("Introduzca número 7:");
    scanf("%d",&num7);

    if (num7>mayor)
    {
       mayor=num7;
    }
    else if (num7<menor)
    {
       menor=num7;
    }
   
    printf("Introduzca número 8:");
    scanf("%d",&num8);

    if (num8>mayor)
    {
       mayor=num8;
    }
    else if (num8<menor)
    {
       menor=num8;
    }
   
    printf("Introduzca número 9:");
    scanf("%d",&num9);

    if (num9>mayor)
    {
       mayor=num9;
    }
    else if (num9<menor)
    {
       menor=num9;
    }
   
    printf("Introduzca número 10:");
    scanf("%d",&num10);

    if (num10>mayor)
    {
       mayor=num10;
    }
    else if (num10<menor)
    {
       menor=num10;
    }

    printf("El mayor es:%d\n",mayor);
    printf("El menor es:%d\n",menor);

    system("PAUSE");     
    return 0;
}
