#include <stdio.h>

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
void Transformer_Valeur(int (*t)[10]){
    for (int i = 0 ; i<10 ; i++){
        for (int j = 0 ; j<10 ; j++){
                // Vérifier si tous les voisins sont nuls
                if (t[i][j] != 0 && !((i > 0 && t[i-1][j] != 0) || 
                    (i < 9 && t[i+1][j] != 0) ||
                    (j > 0 && t[i][j-1] != 0) || 
                    (j < 9 && t[i][j+1] != 0) ||
                    (i > 0 && j > 0 && t[i-1][j-1] != 0) || 
                    (i > 0 && j < 9 && t[i-1][j+1] != 0) ||
                    (i < 9 && j > 0 && t[i+1][j-1] != 0) || 
                    (i < 9 && j < 9 && t[i+1][j+1] != 0))) {
                        t[i][j] = 0;
                } 
        }
    }
}
int main()
{
    /*
    int t[10][10] = {
    {1, 0, 1, 0, 0, 0, 1, 0, 0, 1},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 1, 0, 1, 0, 1, 1, 1, 1, 0},
    {0, 0, 0, 0, 0, 0, 1, 0, 0, 1},
    {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 0, 0, 1, 1, 0, 0},
    {0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
    {0, 0, 0, 1, 0, 0, 1, 0, 0, 1},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {1, 0, 0, 0, 0, 1, 1, 1, 1, 1}
    };
    */
    int t[10][10] ;
    for (int i = 0 ; i<10 ; i++){
        for (int j = 0 ; j<10 ; j++)
            scanf("%d",&(t[i][j])) ;
    }
    printf("Le nombre des zeros presents dans la derniere ligne est : %d",Compter_zero_ligne(t,9)) ;
    printf("\n") ;
    printf("lignes contenants le plus grand nombre des zeros est : ") ;
    printf("\n") ;
    Transformer_Valeur(t) ;

    return 0;
}
