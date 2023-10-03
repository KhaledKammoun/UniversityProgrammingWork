#include <stdio.h>
int main()
{
    int n1;
    do
    {
        printf("donner un entier : ") ;
        scanf("%d",&n1) ;
    }while (n1<=0);
    for (int n = 1 ;n<=n1;n++)
    {
            bool test=1 ;//tester si il est premier ou non
            for (int i = 2 ; i<n ; i++)
            {
                if (n%i==0 )
                {
                    test=0 ;
                    break ;
                }
            }if (test && n!=1)
                printf(" %d |",n) ;
    }return 0 ;
}
