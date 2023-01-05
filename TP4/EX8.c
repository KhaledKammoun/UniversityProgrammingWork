#include <stdio.h>
int main()
{
    int n , m ;
    scanf("%d %d",&n,&m) ;
    int t[n][m] ;
    int som_ligne[n]={0} ;
    int som_col[m]={0} ;
    int test_ligne=1,test_col=1 ;
    for (int i = 0 ;i<n ;i++){
        for (int j =0 ;j<m;j++)
            scanf("%d",&t[i][j]) ;
    }
    int i=0 ;

    while((test_ligne==1 && test_col==1) && i<n){
        for (int j = 0 ;j<m ;j++){
            som_ligne[i]+=t[i][j] ;
            som_col[i]+=t[j][i] ;
        }
        if (i>0 && som_ligne[i-1]!=som_ligne[i])
            test_ligne=0 ;
        if (i>0 && som_col[i-1]!=som_col[i])
            test_col=0 ;
        i++ ;
    }
    if (test_ligne==1 || test_col==1 )
        printf("Cette matrice est parfait" ) ;
    else
        printf("Cette matrice est non parfait")
    return 0;
}
