#include <stdio.h>

int main()
{
    int n, m ;
    scanf("%d %d",&n,&m) ;
    int a[n+m]={0},b[m] ;
    for (int i =0 ;i<n ; i++)
        scanf("%d",&a[i]) ;
    for (int i =0 ;i<m ; i++)
        scanf("%d",&b[i]) ;
    int occ=0,i=0 ;
    while(i<(n-m+1) && occ<=3){
        int j = i,test=1 ;
        while(j<(i+m) && test==1){
            if (a[j]==b[j-i])
                j++ ;
            else
                test=0 ;
        }
        if (test==1)
            occ++ ;
        if (occ==3){
            for (int k=i+m ; k<n ; k++){
                a[k-m]=a[k] ;
            }
            n-=m ;
        }
    }
    for (int i = 0 ;i<n ;i ++)
        printf("%d ",a[i]) ;
    return 0;
}
