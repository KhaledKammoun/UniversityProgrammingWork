#include <stdio.h>
int main()
{
    int *p1,*p2,n1,n2 ;
    scanf("%d %d",&n1,&n2) ;
    p1=&n1;
    p2=&n2;
    printf("leur somme est : %d",(*p1)+(*p2)) ;
    return 0;
}
