#include <stdio.h>
int main ()
{
    int n,l,n1 ;
    do
    {
        scanf("%d",&n) ;
    }while (n<=0) ;
    n1=n ;
    while (n1!=0)
    {
        n1/=10 ;
        l+=1 ;
    }
    int x1=n , s=0,p=1;
    for (int i = 0 ;i<l ;i++)
    {
        s+=(x1%10) ;
        p*=(x1%10) ;
        x1=x1/10 ;
    }
    float m ;
    m=s/l ;
    printf("Leur sommes  : %d\n",s) ;
    printf("Leur produits : %d\n",p) ;
    printf("Leur moyennes : %f\n",m) ;
}
