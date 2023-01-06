#include <stdio.h>
#include <malloc.h>
int main()
{
    int *t,n ;
    scanf("%d",&n) ;
    t=(int*)malloc(n) ;
    for (int i = 0 ; i<n ; i++)
        scanf("%d",(t+i)) ;
    for (int i = 0 ; i<n ; i++)
        printf("%d ",*(t+i)) ;
    free(t) ;
    return 0;
}
