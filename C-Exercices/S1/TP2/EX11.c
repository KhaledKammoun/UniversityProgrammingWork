#include <stdio.h>
#include <string.h>
int main()
{
    int ascii ;
    char c ;
    printf("donner un caractere : ") ;
    scanf("%c",&c) ;
    ascii=(int) c ;
    if (strchr("0123456789",c))
        printf("Nombre : %c code : %d\n",c,c) ;
    else if (ascii>64 && ascii<123)
        printf("Caractere : %c code : %d\n",c,c) ;
    else
        printf("Symbole : %c code : %d\n",c,c) ;
    if (ascii>64 && ascii<97)
        printf("%c est Majus son Minus est : %c",ascii,ascii+32) ;
    else if (ascii>96 && ascii<123)
        printf("%c est Minus son Majus est : %c",ascii,ascii-32) ;
    else
        printf("Erreur") ;
}
