#include <stdio.h>
#include <string.h>
#include <malloc.h>
int recherche(char *ch1 , char*ch2){
    for (char* i = ch2 ; i-ch2<strlen(ch2) ; i++){
        if (strncmp(ch1,i,strlen(ch1))==0)
            return i-ch2 ;
    }
    return -1 ;
}
int main(){
    char *ch1 , *ch2 ;
    ch1 = (char*)malloc(100*sizeof(char)) ;
    ch2 = (char*)malloc(100*sizeof(char)) ;
    printf("donner ch1 : ") ;
    scanf("%s",ch1) ;
    printf("donner ch2 : ") ;
    scanf("%s",ch2) ;
    int test = recherche(ch1,ch2) ;
    if (test == -1)
        printf("ch1 n'est pas incluse dans ch2");
    else 
        printf("premiere occurrence de ch1 dans ch2 est dans l'indice : %d", test);
}