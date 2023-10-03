#include <stdio.h>
#include <string.h>
int recherche(char ch1[100] , char ch2[100]){
    for (int i = 0 ; i<strlen(ch2) ; i++){
        if (strncmp(ch1,ch2+i,strlen(ch1))==0)
            return i ;
    }
    return -1 ;
}
int main(){
    char ch1[100] , ch2[100] ;
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
