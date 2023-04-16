#include <stdio.h>
#include <string.h>
#include <malloc.h>
void inverse(char*ch , char*ch1){
    char *aux ;
    aux = (char*)malloc(100*sizeof(char)) ;
    strcpy(aux,ch) ;
    strcpy(ch,ch1) ;
    strcpy(ch1,aux) ;
}
int main(){
    char *ch , *ch1 ;
    ch = (char*)malloc(100*sizeof(char)) ;
    ch1 = (char*)malloc(100*sizeof(char)) ;
    printf("donner ch : ") ;
    scanf("%s",ch) ;
    printf("donner ch1 : ") ;
    scanf("%s",ch1) ;
    inverse(ch,ch1) ;
    printf("ch : %s\n",ch) ;
    printf("ch1 : %s",ch1) ;
}