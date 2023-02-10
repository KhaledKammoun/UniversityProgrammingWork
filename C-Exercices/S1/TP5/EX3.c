#include <stdio.h>
int main()
{
    int n,s=0 ;
    scanf("%d",&n) ;
    int tab[n] ;
    int *t=tab ;

    for (int i=0 ; i<n ; i++){
        scanf("%d",(t+i)) ;
        s+=*(t+i) ;
    }
    /*
    2°methode :
    for (int *i=t ; i<(t+n) ; i++){
        scanf("%d",i) ;
        s+=*(i) ;
    }
    */
    printf("%d",s) ;
    return 0;
}
