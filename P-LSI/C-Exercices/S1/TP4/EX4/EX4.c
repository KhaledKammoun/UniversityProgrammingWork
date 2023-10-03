#include <stdio.h>
int main()
{
    int n , m ;
    printf("Donner n et m : ") ;
    scanf("%d %d",&n,&m) ;
    int a[n],b[m] ;
    printf("Donner les elements de A : ") ;
    for (int i =0 ;i<n ; i++)
        scanf("%d",&a[i]) ;
    printf("Donner les elements de B : ") ;
    for (int i =0 ;i<m ; i++)
        scanf("%d",&b[i]) ;
    int occ=0 ;
    for (int i =0 ; i<n ; i++){
        int j = 0 ,test=0;
        while(j<m && test==0){
            if (a[i]==b[j] && b[j]!='*'){
                occ++ ;
                test=1 ;
                b[j]='*' ;
            }
            j++ ;
        }
    }
    if (occ==n)
        printf("Le tableau A est inclus dans B") ;
    else
        printf("Le tableau A n'est pas inclus dans B") ;
    return 0;
}
