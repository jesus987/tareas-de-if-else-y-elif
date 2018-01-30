#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int num1;
           
            printf("Introduzca un número:");
    scanf("%d",&num1);
   
    if (num1>100){
       printf("Es mayor\n");
    }
    else
    {
       printf("Es menor\n");
    }
   
    system("PAUSE");     
    return 0;
}
