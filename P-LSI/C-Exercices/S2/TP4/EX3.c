#include <stdio.h>
#include <string.h>
struct client{
    char RIB[20], nom[30], prenom[30], CIN[10] ;
    float Solde ;
};
void saisie_clients(struct client *C , int n){
    for (int i = 0 ; i<n ; i++){
        printf("Client n*%d : \n",i) ;
        printf("donner RIB : ") ;
        scanf("%s",C[i].RIB) ;
        printf("donner nom : ") ;
        scanf("%s",C[i].nom) ;
        printf("donner prenom : ") ;
        scanf("%s",C[i].prenom) ;
        printf("donner CIN : ") ;
        scanf("%s",C[i].CIN) ;
        printf("donner Solde : ") ;
        scanf("%f",&C[i].Solde) ;
    }
}
void affiche_clients(struct client C[20], int T[20], int nbr){
    for (int i = 0 ; i<nbr ; i++){
        printf("\nClient n*%d\n",T[i]) ;
        printf("RIB : %s\n",C[T[i]].RIB) ;
        printf("nom : %s\n",C[T[i]].nom) ;
        printf("prenom : %s\n",C[T[i]].prenom) ;
        printf("CIN : %s\n",C[T[i]].CIN) ;
        printf("Solde : %.2f\n",C[T[i]].Solde) ;
    }
}
int client_au_rouge(struct client C[20], int n, int T[20]){
    int nbr = 0 ;
    for (int i = 0 ; i<n ; i++){
        if (C[i].Solde<0){
            T[nbr] = i ;
            nbr++ ;
        }
    }
    return nbr ;
}

int main()
{
    struct client C[100] ;
    int T[20] ,n, nbr;
    printf("donner n : ") ;
    scanf("%d",&n) ;
    saisie_clients(C,n) ;
    nbr = client_au_rouge(C,n,T) ;
    if (nbr>0){
        affiche_clients(C,T,nbr) ;
        printf("Nombre de clients au rouge : %d\n", nbr);
    }
    else
        printf("nbr = 0") ;
    return 0;
}
