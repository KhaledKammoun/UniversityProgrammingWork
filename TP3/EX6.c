#include <stdio.h>
int main()
{
    for (int i = 1 ; i<10 ;i++)
    {
        for (int j =1 ; j<10 ; j++)
        {
            printf("%d ",(i*j)) ;
        }
        printf("\n") ;
    }
    printf("\n") ;
    //ex 2
    int m , n ;
    do
    {
        printf("donner un entier m : ") ;
        scanf("%d",&m) ;
    }while (m>20) ;
    printf("donner n : ") ;
    scanf("%d",&n) ;
    for (int i = 1 ;i<(m+1) ; i++)
    {
        for (int j = 1 ; j<(n+1) ; j++)
            printf("%d ",(i*j)) ;
        printf("\n") ;
    }
}
