#include <stdio.h>

int main ()
{
    int ascii ;
    char c ;
    do
    {
        printf("donner un caractere : ") ;
        scanf("%s",&c) ;
        ascii=(int) c ;
    }while ((ascii >120) || (ascii<64) || (ascii==90)) ;
    printf("La lettre qui vient juste apres '%c' est : %c",ascii,ascii+1) ;
    return 0 ;
}
