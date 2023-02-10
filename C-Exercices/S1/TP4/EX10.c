#include <stdio.h>
int main()
{
    int n ,m;
    scanf("%d %d",&n,&m) ;
    int t[n][m] ;
    int prem=1 ;
    int t_prem[prem]={0} ;
    prem=0 ;
    for (int i = 0 ; i<n ; i++){
        for (int j =0 ;j<m ; j++){
            scanf("%d",&t[i][j]) ;
            bool test=1 ;//tester si il est premier ou non
            for (int k = 2 ; k<t[i][j] ; k++)
            {
                if (t[i][j]%k==0 ){
                    test=0 ;
                    break ;
                }
            }
            if (test==1 && t[i][j]>1){
                t_prem[prem]=t[i][j] ;
                prem++ ;
            }
        }
    }
    for (int i = 0 ;i<prem ; i++)
        printf("%d ",t_prem[i]) ;
    return 0;
}
