#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define LONG 5
int main()
{
    char s[100] ;
    do{
        printf("donner une chaine de caractére : ") ;
        gets(s) ;
    }while (strlen(s)<LONG) ;
    int n = strlen(s) ;
    for (char*i=s ; *i!='\0' ;i++){
        if (!(isalnum(*i)))
            *i=' ' ;
    }
    printf("1 : %s\n",s) ;
    int car = 0; //'car' pour les espaces au debut de la chaine
    char*p = s ;
    while (p<s+n-1){
        if (*p!=' ')
            car++ ;
        if (car==0 || (*p==' ' && *(p+1)==' ')){
            char* j = p+1;
            if (car == 0)
                j = p ;
            for (j; j<s+n-1 ; j++){
                *j=*(j+1) ;
            }
            *(s+n-1)='\0' ;
            n-- ;
        }
        else{
            p++ ;
            if (*p==' ' && p==s+n-1){  //pour les espaces à la fin de la chaine
                *p='\0' ;
                p-- ;
            }
        }
    }
    printf("2 : %s\n",s) ;
    //question 4 :
    //abcest est --> abcêtre être
    char add_ch_1[] = "être" ;
    char tmp_1[] ="est";
    char*p1 = s ;
    p=s ;
    while(p<s+(n-strlen(tmp_1)+1)){
        if (*p=='e' && *(p+1)=='s' && *(p+2)=='t'){
            p1=p ;
            char* k = add_ch_1 ;
            while(p-p1<strlen(add_ch_1)){
                if (p-p1>=strlen(tmp_1)){//decalage
                    for (char* j = s+n ; j>p; j--){
                        *j=*(j-1) ;
                    }
                    n++ ;
                    
                }
                *p=*k ;
                k++ ;
                p++ ;
            }
        }
        else
            p++ ;
    }
    printf("3 : %s\n",s) ;
    //question 5 :
    //abcer ser -->abcons sons
    char add_ch_2[] = "ons" ;
    char tmp_2[] ="er";
    p1 = s ;
    p=s+1 ;
    while(p<s+(n-strlen(tmp_2))+1){
        if ( *(p-1)!=' ' && *p=='e' && *(p+1)=='r' && (p==s+(n-strlen(tmp_2)) || *(p+2)==' ')){
            p1=p ;
            char*k = add_ch_2 ;
            while(p-p1<strlen(add_ch_2)){

                if (p-p1>=strlen(tmp_2)){//decalage
                    for (char*j = s+n ; j>p; j--){
                        *j=*(j-1) ;
                    }
                    n++ ;

                }

                *p=*k ;
                k++ ;
                p++ ;
            }
        }
        else
            p++ ;
    }
    printf("4 : %s",s) ;
    return 0;
}