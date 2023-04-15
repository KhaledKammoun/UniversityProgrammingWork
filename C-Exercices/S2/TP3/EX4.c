#include <stdio.h>
#include <string.h>
int recherche(char *ch , char*ch1){
    for (int i = 0 ; i<strlen(ch1)-strlen(ch)+1 ; i++){
        if (strncmp(ch,ch1+i,strlen(ch))==0)
            return i ;
    }
    return -1 ;
}
int main(){
    char ch[100] , ch1[100] ;
    printf("donner ch : ") ;
    scanf("%s",&ch) ;
    printf("donner ch1 : ") ;
    scanf("%s",&ch1) ;
    int test = recherche(ch,ch1) ;
    if (test == -1)
        printf("ch n'est pas incluse dans ch1");
    else 
        printf("première occurrence de ch dans ch1 est dans l'indice : %d", test);
}