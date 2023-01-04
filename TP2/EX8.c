#include <stdio.h>
#define min(i,j) ( (i<j) ? (i) : (j) )
int main()
{
    float x,y ;
    do
    {
       printf("donner x : ") ;
        scanf("%f",&x) ;
        printf("donner y : ") ;
        scanf("%f",&y)  ;
    }while (x==y) ;
    printf("le minimum entre x et y : %f",min(x,y)) ;
    return 0 ;

}
