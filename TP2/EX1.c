#include <stdio.h>
int main()
{
    float salaire,taux ;
    int h ;
    printf("donner le taux horaire : ") ;
    scanf("%f",&taux) ;
    printf("donner nombre d'heure : ") ;
    scanf("%d",&h) ;
    if (h<=39)
    {
        salaire=h*taux;
    }
    else if (h<=44)
    {
        salaire=39*taux +(h-39)*(taux*1.2) ;
    }
    else if (h<=49)
    {
        salaire = 39*taux + 5*(taux*1.2) + (h-44)*(taux*1.5) ;
    }
    else
        salaire = 39*taux + 5*(taux*1.2) + 5*(taux*1.5) + (h-49)*(taux*1.8) ;
    printf("Le salaire est %f",salaire) ;
    return 0 ;
}

