#include <stdio.h>

int main()
{
    int N;
    printf("donner un entier N : ") ;
    scanf("%d",&N) ;
    for (int i = 0 ; i<N ; i++)
        printf ("%c",'*');    // n ° 1
    printf("\n") ;
    int s = 0,i=0 ;
    while (N>i)
    {
        s+=(i*i) ;
        i++ ;   // n ° 2
    }
    s=0 ;
    int N1=N ;
    for (int i = 0 ;i<N ;i++)
    {
        N1-=7 ;
        if (N1<=0)
            break ;
        s++;          // n ° 3
    }
    i=1 ;
    int p=1 ;
    while (i<=N)
    {
        p*=i ;
        i+=2 ;
    }            // n ° 4
    return 0 ;
}
