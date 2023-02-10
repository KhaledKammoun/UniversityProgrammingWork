#include <stdio.h>
int main()
{
    int n;
    do
    {
        scanf("%d",&n) ;
        int x=n , l=0;
        while (x!=0)
        {
            l+=1 ;
            x/=10 ;
        }
        if (l==3)
            break ;
    }while (n<40 || n>60) ;

    int som=0 ,som_paire=0 ,som_impaire=0 ;

    for (int i = 1 ; i<(n+1) ; i++)
    {
        som+=i ;
        if (i%2==0)
            som_paire+=i ;
        else
            som_impaire+=i ;
    }
    printf("La somme des entiers de %d est : %d\n",n,som) ;
    printf("La somme paire des entiers de %d est : %d\n",n,som_paire) ;
    printf("La somme impaire des entiers de %d est : %d",n,som_impaire) ;
    return 0 ;
}
