#include <stdio.h>
int main()
{
    int n ;
    do{
        scanf("%d",&n) ;
    }while(n<=1 && n>=20) ;
    int t[n]={0} ;
    for (int i =0 ;i<n ; i++)
        scanf("%d",&t[i]) ;
    int i=0,occ=0 ,b=0;
    while(i<=n && b==0){
        if (t[i]==1 && i<n)
            occ++ ;
        else {
            if (occ%2!=0 && occ!=0)
                b=1 ;
            else
                occ=0 ;
        }
    i++ ;
    }
    if (b==1)
        printf("Valide") ;
    else
        printf("Non valide") ;
    return 0;
}
