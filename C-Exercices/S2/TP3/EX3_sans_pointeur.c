#include <stdio.h>
#include <string.h>
void inverse(char ch[100] , char ch1[100]){
    char aux[100] ;
    strcpy(aux,ch) ;
    strcpy(ch,ch1) ;
    strcpy(ch1,aux) ;
}
int main(){
    char ch[100] , ch1[100] ;
    printf("donner ch : ") ;
    scanf("%s",ch) ;
    printf("donner ch1 : ") ;
    scanf("%s",ch1) ;
    inverse(ch,ch1) ;
    printf("ch : %s\n",ch) ;
    printf("ch1 : %s",ch1) ;
}
