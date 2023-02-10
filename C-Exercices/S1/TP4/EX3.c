#include <stdio.h>

int main()
{
    int n ,np=1,nn=1;
    do {
        printf("Donner n : ") ;
        scanf("%d",&n) ;
    }while(n<=0 || n>=50) ;
    int t[n],tp[np],tn[nn] ;

    np=nn=0 ;
    printf("Donner les elements de T : ") ;
    for (int i = 0 ;i<n ; i++){
        scanf("%d",&t[i]) ;
        if (t[i]>=0){
            tp[np]=t[i] ; //methode de pointeur : *(tp+np)=*(t+i) ;
            np++ ;}
        else {
            tn[nn]=t[i] ;
            nn++ ;}
    }
    printf("Les entiers positifs : ") ;
    for (int i = 0 ;i<np ;i++)
        printf("%d ",tp[i]) ;
    printf("\n") ;
    printf("Les entiers negatifs : ") ;
    for (int i = 0 ;i<nn ;i++)
        printf("%d ",tn[i]) ;
    return 0;
}
