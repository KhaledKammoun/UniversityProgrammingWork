#include <stdio.h>
int main ()
{
    int n,l ;
    do
    {
        scanf("%d",&n) ;
    }while (n==0) ;

    int x1=n , s=0,p=1;
    do
    {
        s+=(x1%10) ;
        p*=(x1%10) ;
        x1=x1/10 ;
        l+=1;
    }while (x1!=0) ;
    float m ;
    m=s/l ;
    printf("Leur sommes  : %d\n",s) ;
    printf("Leur produits : %d\n",p) ;
    printf("Leur moyennes : %f\n",m) ;
}
