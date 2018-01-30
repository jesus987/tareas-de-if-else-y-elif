#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int opcion;
     printf("Seleccione opción:\n");
     printf("1 - Archivo\n");
     printf("2 - Buscar\n");
     printf("3 - Salir\n");
    
     scanf("%d",&opcion);

     if (opcion!=1 && opcion!=2 && opcion!=3)
     {
         printf("La opción NO es correcta.\n");
     }
     else
     {
         printf("La opción es correcta.\n");
     }                  

system("PAUSE");     
return 0;
}
