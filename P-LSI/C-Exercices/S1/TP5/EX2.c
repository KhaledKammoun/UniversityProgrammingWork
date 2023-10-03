#include <stdio.h>
int main()
{
    char *p1,*p2,c1,c2 ;
    scanf("%c %c",&c1,&c2) ;
    p1=&c1;
    p2=&c2 ;
    char x=*p1;
    *p1=*p2;
    *p2=x ;
    printf("%c %c",*p1,*p2) ;
    return 0;
}
