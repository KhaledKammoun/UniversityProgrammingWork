#include <stdio.h>
int main()
{
    int n ;
    printf("Donner n : ") ;
    scanf("%d",&n) ;
    int t[n] ;
    printf("Donner les elements de A : ") ;
    scanf("%d",&t[0]) ;
    for (int i = 1 ;i<n ;i++){
        do{
            scanf("%d",&t[i]) ;
        }while (t[i]<t[i-1]) ;
    }
    for (int i = 0 ;i<(n/2) ; i++){

        int x=t[i] ;
        t[i]=t[n-i-1] ;
        t[n-i-1]=x ;
    }
    printf("l'inverse de A est : ") ;
    for (int i = 0 ;i<n ; i++)
        printf("%d ",t[i]) ;
    return 0 ;
}
