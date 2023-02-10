#include <stdio.h>
int main ()
{
    int j,h ;
    do
    {
        printf("donner le numero du jour : ") ;
        scanf("%d",&j) ;
        printf("donner le numero du l'heure : ") ;
        scanf("%d",&h) ;
    }while (j<1 || j>7 || h<0 || h>24) ;
    switch(j)
    {
    case 1 :
        {printf("Lundi\n") ;break ;}
    case 2 :
        {printf("Mardi\n") ;break ;}
    case 3 :
        {printf("Mercredi\n") ;break ;}
    case 4 :
        {printf("Jeudi\n") ;break ;}
    case 5 :
        {printf("Vendredi\n") ;break ;}
    case 6 :
        {printf("Samedi\n") ;break ;}
    case 7 :
        {printf("Dimanche\n") ;break ;}
    }
    int n_e=((j-1)*24)+h ;
    printf("Le nombre d'heure ecoulees : %d\n",n_e) ;
    printf("%d %d %d",j,n_e,h) ;
}
