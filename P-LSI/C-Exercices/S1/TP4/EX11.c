#include <stdio.h>
int main()
{
    int m , n ;
    scanf("%d %d",&m,&n) ;
    int t[m][n] ;
    int Max=0,Min ;
    scanf("%d",&t[0][0]) ;
    Min=t[0][0] ;
    for (int i = 0 ; i<m ; i++){
        for (int j=1 ;j<n ; j++){
            scanf("%d",&t[i][j]) ;
            if (t[i][j]>Max)
                Max=t[i][j] ;
            if (t[i][j]<Min)
                Min=t[i][j] ;
        }
    }
    printf("Min = %d | Max = %d",Min,Max) ;
    return 0;
}
