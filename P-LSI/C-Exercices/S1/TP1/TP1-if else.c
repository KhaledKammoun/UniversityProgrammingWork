#include <stdio.h>
#define PI 3.14
int main()
{
    int a,b ;
    char c ;
    printf("donner a : ") ;
    scanf("%d",&a) ;
    printf("donner b : ") ;
    scanf("%d",&b) ;
    printf("donner un caractere : ") ;
    scanf("%s",&c) ;

    if ((c=='R')|| (c=='r') ){printf("La surface est %d",a*b);}
    if ((c=='C')||(c=='c')){printf("La surface est %d",a*a);}
    if ((c=='O') ||(c=='o')){printf("La surface est %f",(a/2)*(a/2)*PI);}
    if ((c=='T') || (c=='t')){printf("La surface est %f",((a*(b/2))/2));}
    return 0 ;
}
