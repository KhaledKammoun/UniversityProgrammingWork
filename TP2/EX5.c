#include <stdio.h>
#include <math.h>
int main()
{
    int a,b,c,d ;
    float r_d ;
    printf("donner a : ") ;
    scanf("%d",&a) ;
    printf("donner b : ") ;
    scanf("%d",&b) ;
    printf("donner c : ") ;
    scanf("%d",&c) ;
    d=(pow(b,2)-4*(a*c)) ;

    if (d>0)
        {
            r_d=sqrt(d) ;
            printf("il y a 2 possibilite\n");
            printf("x1 = %f ; x2 = %f",(-b-r_d)/(2*a),(-b+r_d)/(2*a)) ;
        }
    else if (d==0)
        {
            printf("il y a une seule possibilite") ;
            float x ;
            x=-b/(2*a) ;
            printf("x = %f",x) ;
        }
    else
        printf("Impossible") ;
    return 0 ;

}
