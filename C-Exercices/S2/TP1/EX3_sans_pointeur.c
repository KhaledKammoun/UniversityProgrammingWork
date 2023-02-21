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
    for (int i=0 ; i<n ;i++){
        if (!(isalnum(s[i])))
            s[i]=' ' ;
    }
    printf("1 : %s\n",s) ;
    int i = 0,car = 0; //'car' pour les espaces au debut de la chaine

    while (i<n-1){
        if (s[i]!=' ')
            car++ ;
        if (car==0 || (s[i]==' ' && s[i+1]==' ')){
            int j = i+1;
            if (car == 0)
                j = i ;
            for (j; j<n-1 ; j++){
                s[j]=s[j+1] ;
            }
            s[n-1]='\0' ;
            n-- ;
        }
        else{
            i++ ;
            if (s[i]==' ' && i==n-1){  //pour les espaces à la fin de la chaine
                s[i]='\0' ;
                i-- ;
            }
        }
    }
    printf("2 : %s\n",s) ;
    //question 4 :
    //abcest est --> abcêtre être
    char add_ch_1[] = "être" ;
    char tmp_1[] ="est";
    int l = 0 ;
    i=0 ;
    while(i<(n-strlen(tmp_1)+1)){
        if (s[i]=='e' && s[i+1]=='s' && s[i+2]=='t'){
            l=i ;
            int k = 0 ;
            while(i-l<strlen(add_ch_1)){
                if (i-l>=strlen(tmp_1)){//decalage
                    for (int j = n ; j>i; j--){
                        s[j]=s[j-1] ;
                    }
                    n++ ;
                    
                }
                s[i]=add_ch_1[k] ;
                k++ ;
                i++ ;
            }
        }
        else
            i++ ;
    }
    printf("3 : %s\n",s) ;
    //question 5 :
    //abcer er -->abcons ons
    char add_ch_2[] = "ons" ;
    char tmp_2[] ="er";
    l = 0 ;
    i=1 ;
    while(i<(n-strlen(tmp_2))+1){
        if ( s[i-1]!=' ' && s[i]=='e' && s[i+1]=='r' && (i==(n-strlen(tmp_2)) || s[i+2]==' ')){
            l=i ;
            int k = 0 ;
            while(i-l<strlen(add_ch_2)){

                if (i-l>=strlen(tmp_2)){//decalage
                    for (int j = n ; j>i; j--){
                        s[j]=s[j-1] ;
                    }
                    n++ ;

                }

                s[i]=add_ch_2[k] ;
                k++ ;
                i++ ;
            }
        }
        else
            i++ ;
    }
    printf("4 : %s",s) ;
    return 0;
}