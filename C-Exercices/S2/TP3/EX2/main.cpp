#include <iostream>

using namespace std;
int Compter_zero_ligne(int t[10][10], int p){
    int zero= 0 ;
    for (int i = 0 ; i<10 ; i++){
        if (t[p][i]==0)
            zero++ ;
    }
    return zero ;
}
void  Affiche_ligne (int t[10][10]) {
    int max_len = Compter_zero_ligne(t,0) ;
    for (int i = 1 ; i<10 ; i++){
        if (max_len<Compter_zero_ligne(t,i))
            max_len=Compter_zero_ligne(t,i) ;
    }
    for (int i =0 ; i<10 ; i++){
        if (Compter_zero_ligne(t,i)==max_len){
            printf("%d ",i) ;
        }
    }
    printf("\n") ;
}
int main()
{
    int t[10][10] = {
    {0, 0, 1, 0, 0, 0, 1, 0, 0, 0},
    {0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
    {0, 1, 0, 1, 0, 1, 1, 1, 1, 0},
    {0, 0, 0, 0, 1, 0, 1, 0, 0, 1},
    {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 0, 0, 1, 1, 0, 0},
    {0, 0, 0, 0, 0, 1, 0, 0, 1, 0},
    {0, 0, 0, 1, 0, 0, 1, 0, 0, 1},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {0, 0, 0, 0, 0, 1, 1, 1, 1, 0}
};/*
    for (int i = 0 ; i<2 ; i++){
        for (int j = 0 ; j<2 ; j++)
            scanf("%d",&(t[i][j])) ;
    }
    */
    int p ;
    printf("Donner p : ") ;
    scanf("%d",&p) ;
    int nb_zero = Compter_zero_ligne(t,p) ;
    printf("Le nombre de zero dans cette matrix est %d",nb_zero) ;
    printf("\n") ;
    for (int i = 0 ; i<10 ; i++){
        for (int j = 0 ; j<10 ; j++)
            printf("%d ",t[i][j]) ;
        printf("\n") ;
    }
    printf("Les lignes qui contient le plus grand nb de zero est ") ;
    Affiche_ligne(t) ;
    return 0;
}

//rania.boujelbene@enis.tn
