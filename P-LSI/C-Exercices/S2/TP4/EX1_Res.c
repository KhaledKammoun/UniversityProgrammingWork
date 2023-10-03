#include <stdio.h>
struct livre
{
    char titre[200], nom[100] ;
    int annee ;
};
struct bibliotheque
{
    struct livre tab[100] ;
    int nb_livre ;
};
struct bibliotheque Fsaisie(struct bibliotheque B){
    for (int i = 0 ; i<B.nb_livre ; i++){
        printf("Livre N#%d\nDonner le titre du livre : ",i+1) ;
        scanf("%s",B.tab[i].titre) ;
        printf("Donner le nom de l'auteur : ") ;
        scanf("%s",B.tab[i].nom) ;
        printf("Donner l'annee de son edition : ") ;
        scanf("%d",&B.tab[i].annee) ;
    }
    return B ;
}
void Faffiche(struct bibliotheque B){
    int j = 0 ;
    for (int i = 0 ; i<B.nb_livre ; i++){
        if (B.tab[i].annee>=2000){
            printf("Livre N#%d\n",j++) ;
            printf("Titre : %s\n",B.tab[i].titre) ;
            printf("Nom de l'auteur : %s\n",B.tab[i].nom) ;
            printf("Annee de son edition : %d\n",B.tab[i].annee) ;
            printf("---------------\n") ;
        }
    }
}
void Fsupprime (struct bibliotheque *B){
    for (int i = 0 ; i<B->nb_livre ; i++){
        if (B->tab[i].nom=="ali"){
            for (int j = i ; j<B->nb_livre-1 ; j++)
                B->tab[j] = B->tab[j+1] ; 
            B->nb_livre-- ;
            break ;
        }
    }
}
int main(){
    struct bibliotheque BIB ;
    BIB.nb_livre = 0 ;
    int N ;
    do{
        printf("Donner le nombre de livres : ") ;
        scanf("%d",&N) ;
    }while (N>=100) ;
    BIB.nb_livre = N ;
    BIB = Fsaisie(BIB) ;
    printf("---------------\nLes livres dont l'annee d'edition est sup ou egal a 2000\n") ;
    printf("---------------\n") ;
    Faffiche(BIB) ;
    int nb_livres_avant = BIB.nb_livre ;
    Fsupprime(&BIB) ;
    if (BIB.nb_livre==nb_livres_avant)
        printf("le nombre des livres de BIB est le meme apres l'appel a Fsupprime\n") ;
    else 
        printf("le nombre des livres de BIB n'est pas le meme apres l'appel a Fsupprime\n") ;
}