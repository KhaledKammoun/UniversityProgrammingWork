#include <stdio.h>
int main()
{
    int n ,s=0;
    scanf("%d",&n) ;
    for (int i = 1 ;i<((n/2)+1) ; i++)
    {

        if ((n%i)==0)
            s+=i ;
    }
    if (s==n)
        printf("%d est un nombre parfait",n) ;
    else
        printf("%d est un nombre non parfait",n) ;
}
