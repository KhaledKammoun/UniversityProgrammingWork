#include <stdio.h>
int main()
{
    int nb_jour ;
    printf("donner un nombre de jour : " ) ;
    scanf("%d",&nb_jour) ;
    if (nb_jour>0 &&nb_jour<=5)
        printf("il y a cours") ;
    else if (nb_jour==6)
        printf("il y a DS") ;
    else printf("On se repose ") ;
    return 0 ;
}
