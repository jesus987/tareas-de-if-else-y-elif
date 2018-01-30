#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            char c;
           
            printf("Introduzca un carácter:");
    scanf("%c",&c);
   
    switch (c)
    {
           case 'a':
                printf ("Es vocal\n");
                break;
           case 'e':
                printf ("Es vocal\n");
                break;
           case 'i':
                printf ("Es vocal\n");
                break;
           case 'o':
                printf ("Es vocal\n");
                break;
           case 'u': 
                printf ("Es vocal\n");
                break;             
           default:
                printf ("No es vocal\n");
                break;
    }
   
    system("PAUSE");     
    return 0;
}
