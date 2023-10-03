#include <stdio.h>
int main ()
{
    int a,b,Min,Max,pgcd,ppcm;
    printf("donner a : ") ;
    scanf("%d",&a) ;
    printf("donner b : ") ;
    scanf("%d",&b) ;
    //Calculer le ppcm
    if (a>b)
    {
        Min=b ;
        Max=a ;
    }
    else
    {
        Min=a ;
        Max=b ;
    }
    int p =Max ;
    while (Max%Min!=0)
        Max+=p ;
    ppcm=Max ;
    //Calculer le pgcd
    int reste ;
    while (b !=0)
    {
        reste = a % b ;
        a=b ;
        b=reste ;
    }
    pgcd=a ;
    printf("%d est le PGCD\n",pgcd) ;
    printf("%d est le PPCM",ppcm) ;
    return 0 ;
}
