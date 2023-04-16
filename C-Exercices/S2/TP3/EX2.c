#include <stdio.h>
#include <string.h>


int main(){
    char ch[100] ;
    
    do{
        printf("donner ch : ") ;
        gets(ch) ;
    }while (strcmp(ch+strlen(ch)-2,"er")!=0) ;
    printf("Verbe : %s\n",ch);
    char *c=ch ;
    while (*c!='e' && *(c+1)!='r'){
        c++ ;
    }
    *c='\0' ;
    char x[100] ;
    
    printf("je %s\n",strcat(strcpy(x,ch),"e"));
    printf("je %s\n",strcat(strcpy(x,ch),"es"));
    printf("je %s\n",strcat(strcpy(x,ch),"e"));
    printf("je %s\n",strcat(strcpy(x,ch),"ons"));
    printf("je %s\n",strcat(strcpy(x,ch),"ez"));
    printf("je %s\n",strcat(strcpy(x,ch),"ent"));
}