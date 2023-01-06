#include <stdio.h>
#include <malloc.h>
int main()
{
    int n ;
    scanf("%d",&n) ;
    int *t=(int*)malloc(n*sizeof(int)) ;
    for (int i = 0 ; i<n ; i++)
        scanf("%d",(t+i)) ;
    for (int i = 0 ; i<n ; i++)
        printf("%d ",*(t+i)) ;
    free(t) ;
    return 0;
}
