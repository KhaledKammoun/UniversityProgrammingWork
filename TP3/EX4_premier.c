#include <stdio.h>
int main()
{
    int n ;
    printf("donner un entier n : ") ;
    scanf("%d",&n) ;
    bool test=1 ;//tester si il est premier ou non
    for (int i = 2 ; i<n ; i++)
    {
        if (n%i==0 )
        {
            test=0 ;
            break ;
        }
    }
    if (test==1 && n>1)
        printf("%d est un nombre premier",n) ;
    else
        printf("%d est un nombre non premier",n) ;
}
