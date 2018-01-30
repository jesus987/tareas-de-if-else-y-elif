#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int horas, minutos, segundos;
           
            printf("Introduzca Hora:");
    scanf("%d",&horas);
            printf("Introduzca Minutos:");
    scanf("%d",&minutos);
            printf("Introduzca Segundos:");
    scanf("%d",&segundos);
           
            segundos=segundos+1;
           
            if (minutos>59)
            {
       minutos=0;
    }
   
    if (horas>23)
            {
       horas=0;
    }
           
            if (segundos>59)
            {
       segundos=0;
       minutos=minutos+1;
      
       if (minutos>59)
       {
          minutos=0;
          horas=horas+1;
          if (horas>23)
          {
             horas=0;
          }
       }
    }
    
    printf("La hora (un segundo después) es: %02d:%02d:%02d \n", horas, minutos, segundos);
    
    system("PAUSE");     
    return 0;
}
