#include <stdio.h>
#include <string.h>
#include <malloc.h>
int recherche(char *ch , char*ch1){
    for (char* i = ch1 ; i-ch1<strlen(ch1) ; i++){
        if (strncmp(ch,i,strlen(ch))==0)
            return i-ch1 ;
    }
    return -1 ;
}
int main(){
    char *ch , *ch1 ;
    ch = (char*)malloc(100*sizeof(char)) ;
    ch1 = (char*)malloc(100*sizeof(char)) ;
    printf("donner ch : ") ;
    scanf("%s",ch) ;
    printf("donner ch1 : ") ;
    scanf("%s",ch1) ;
    int test = recherche(ch,ch1) ;
    if (test == -1)
        printf("ch n'est pas incluse dans ch1");
    else 
        printf("premiere occurrence de ch dans ch1 est dans l'indice : %d", test);
}