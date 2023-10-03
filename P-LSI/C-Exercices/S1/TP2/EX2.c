#include <stdio.h>
#include <string.h>
int main()
{
    char CAR ;
    printf("donner un caractere : ") ;
    scanf("%c",&CAR) ;
    if (CAR=='v')
        printf("voyelle");
    else if (CAR=='c')
        printf("chiffre") ;
    else if (CAR=='a')
        printf("alphabet") ;
    else if (CAR == 's' || CAR == 'p')
        printf("quelconque") ;
    return 0 ;
}
