
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{
    char c ;
    printf("donner un caractere : ") ;
    scanf("%c",&c) ;
    c=tolower(c) ;

    if (strchr("0123456789",c))
        printf("%c est un chiffre",c) ;
    else if  (strchr("oiyeau",c))
    {
        printf("%c est voyelle",c) ;
    }
    else if (strchr("bcdfghjklmnpqrstvwxz",c))
        printf("%c est consonne",c) ;

    else
        printf("%c est un symbole",c) ;
}
