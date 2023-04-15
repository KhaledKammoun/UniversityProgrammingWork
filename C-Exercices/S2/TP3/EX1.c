#include <stdio.h>
#include <string.h>
int lex(char ch[], char ch1[]){
    for (int i = 0 ; ch[i]!='\0' && ch1[i]!='\0' ; i++){
        if (ch[i]>ch1[i])
            return 1 ;
        else if (ch[i]<ch1[i])
            return -1 ;
    }
    if (strlen(ch)==strlen(ch1))
        return 0 ;
    else if (strlen(ch)>strlen(ch1))
        return 1 ;
    else 
        return -1 ;
}
int main(){
    char ch[100],ch1[100] ;
    printf("donner ch : ") ;
    scanf("%s",&ch) ;
    printf("donner ch1 : ") ;
    scanf("%s",&ch1) ;
    int b = lex(ch,ch1) ;
    if(b==1)
        printf("%s precede %s",ch1,ch) ;
    else if (b==0)
        printf("%s == %s",ch,ch1) ;
    else 
        printf("%s precede %s",ch,ch1) ;
        
}