#include <stdio.h>
int main ()
{
    int n,l ;
    while (n==0)
    {
        scanf("%d",&n) ;
    }

    int x1=n , s=0,p=1;
    while (x1!=0)
    {

        s+=(x1%10) ;
        p*=(x1%10) ;
        x1=x1/10 ;
        l+=1;
    }
    float m ;
    m=s/l ;
    printf("Leur sommes  : %d\n",s) ;
    printf("Leur produits : %d\n",p) ;
    printf("Leur moyennes : %f\n",m) ;
}
