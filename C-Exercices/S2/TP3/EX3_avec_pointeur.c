#include <stdio.h>
#include <malloc.h>
int Compter_zero_ligne(int**t, int p){
    int zero= 0 ;
    for (int i = 0 ; i<10 ; i++){
        if (*(*(t+p)+i)==0)
            zero++ ;
    }
    return zero ;
}
void  Affiche_ligne (int**t) {
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
void Transformer_Valeur(int**t){
    for (int i = 0 ; i<10 ; i++){
        for (int j = 0 ; j<10 ; j++){
                if (*(*(t+i)+j) != 0 && !((i > 0 && *(*(t+i-1)+j) != 0) ||
                    (i < 9 && *(*(t+i+1)+j) != 0) ||
                    (j > 0 && *(*(t+i)+j-1) != 0) ||
                    (j < 9 && *(*(t+i)+j+1) != 0) ||
                    (i > 0 && j > 0 && *(*(t+i-1)+j-1) != 0) ||
                    (i > 0 && j < 9 && *(*(t+i-1)+j+1) != 0) ||
                    (i < 9 && j > 0 && *(*(t+i+1)+j-1) != 0) ||
                    (i < 9 && j < 9 && *(*(t+i+1)+j+1) != 0))) {
                        *(*(t+i)+j) = 0;
                }
        }
    }
}
int main()
{


    int **t  ;
    t = (int**)malloc(10*sizeof(int*)) ; //nbre lig
    for (int i = 0 ; i< 10 ; i++)
        t[i] = (int*)malloc(10*sizeof(int)) ; //nbre col

    for (int i = 0 ; i<10 ; i++){
        for (int j = 0 ; j<10 ; j++)
            scanf("%d",*(t+i)+j) ;
    }

    printf("Le nombre des zeros presents dans la derniere ligne est : %d",Compter_zero_ligne(t,9)) ;

    printf("\n") ;
    printf("lignes contenants le plus grand nombre des zeros est : ") ;
    Affiche_ligne(t) ;
    printf("\n") ;
    Transformer_Valeur(t) ;
    for (int i = 0 ; i<10 ; i++){
        for (int j = 0 ; j<10 ; j++)
            printf("%d ",*(*(t+i)+j)) ;
        printf("\n") ;
    }

    for (int i = 0 ; i<10 ;i++)
        free(t[i]) ;
    free(t) ;
    return 0;
}
