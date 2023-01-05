#include <stdio.h>
int main()
{
    int n ;
    scanf("%d",&n) ;
    int t[n] ;
    for (int i = 0 ;i<n ; i++)
        scanf("%d",&t[i]) ;
    int x ;

    scanf("%d",&x) ;
    int occ=0,pre=0,der=0,test_der=0 ;
    for (int i = 0 ;i<n ; i++){
        if (t[i]==x){
            occ+=1 ;
            if (occ==1)
                pre=i ;}
        if (t[n-i-1]==x && test_der==0){
            der=(n-i-1) ;test_der=1;}
    }
    if (occ==0)
        printf("%d appartient au tableau T",x) ;
    else {
        printf("%d appartient au tableau T\n",x) ;
        printf("le nombre d'occurrence de l'entier %d est %d\n",x,occ) ;
        printf("La position de la première apparition de %d est %d\n",x,pre) ;
        printf("La dernière position d'apparition de %d est %d\n",x,der) ;
    }

    return 0;
}
