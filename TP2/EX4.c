#include <stdio.h>
#include <string.h>
int main()
{
    char n[4];
    printf("donner un entier de 3 chiffre : ") ;
    scanf("%s",n) ;
    if (n[0]==n[2])
        printf("%s est symetrique",n) ;
    else
        printf("%s est non symetrique",n) ;
}
