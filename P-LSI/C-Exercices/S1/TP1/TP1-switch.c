#include <stdio.h>
#define PI 3.14
int main ()
{
    char c ;
    int  a,b ;
    printf("donner a et b :") ;
    scanf("%d %d",&a,&b) ;
    printf("donner un caractere : ") ;
    scanf("%s",&c) ;
    switch(c)
    {
    case 'R' :
    case'r'  :  printf("la surtface : rectangle %d",a*b) ;
        break ;
    case 'C' :
    case 'c' :  printf("la surface : carre   %d",a*a) ;
        break ;
    case 'O' :
    case 'o' :  printf("la surface : cercle :  %f",(a/2)*(a/2)*PI) ;
        break ;
    case 'T' :
    case 't' :  printf("la surface : triangle :  %f",a*(b/2)/2) ;
        break ;
    default :   printf("Error") ;
        break ;
    }
    return 0 ;
}
