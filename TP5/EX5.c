#include <stdio.h>
#include <malloc.h>
int main()
{
    int *t,n,m ;
    scanf("%d %d",&n,&m) ;
    t=(int*)malloc(n) ;
    for (int i = 0 ; i<n ; i++)
        (t+i)=(int*)malloc(m) ;
    return 0;
}
