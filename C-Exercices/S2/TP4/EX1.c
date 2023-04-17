#include <stdio.h>
#include <stdbool.h>
struct date {
    int jour, mois, annee ;
};
struct enfant {
    char prenom[20] ;
    struct date date_naissance ;
    char sexe[1] ;
};
struct famille{
    char nom_pere[20], prenom_pere[20], prenom_mere[20] ;
    struct date date_mariage ;
    struct enfant enf[10] ;
};
struct date saisie_date(){
    struct date var_date ;
    do{
        printf("donner le jour : ") ;
        scanf("%d",&var_date.jour) ;
    }while (!(var_date.jour>=1&&var_date.jour<=31)) ;
    do{
        printf("donner le mois : ") ;
        scanf("%d",&var_date.mois) ;
    }while (!(var_date.mois>=1&&var_date.mois<=12)) ;
    do{
        printf("donner le annee : ") ;
        scanf("%d",&var_date.annee) ;
    }while (!(var_date.annee<2012)) ;
    return var_date ;
}
int main()
{
    struct famille F ;
    printf("Donner nom_pere : ") ;
    scanf("%s",F.nom_pere) ;
    printf("Donner prenom_pere : ") ;
    scanf("%s",F.prenom_pere) ;
    printf("Donner prenom_mere : ") ;
    scanf("%s",F.prenom_mere) ;
    printf("Donner date_mariage : \n") ;
    struct date date_mariage ;
    date_mariage = saisie_date() ;
    int nb_famille ;
    printf("Donner nb_famille : ") ;
    scanf("%d",&nb_famille) ;
    for (int i = 0 ; i<nb_famille ; i++){
        printf("Enfant %d\n",i+1) ;
        struct enfant var_enfant ;

        printf("donner prenom : ") ;
        scanf("%s",var_enfant.prenom) ;
        printf("donner sexe(f/m) : ") ;
        scanf("%s",var_enfant.sexe) ;
        printf("donner date_naissance : \n") ;
        var_enfant.date_naissance = saisie_date() ;
        F.enf[i] = var_enfant ;
    }
    int plus_age=0 ;
    for (int i = 0 ;i<nb_famille ; i++){
        if (F.enf[plus_age].date_naissance.annee<F.enf[i].date_naissance.annee)
            plus_age = i ;
    }
    printf("le prenom de l'enfant le plus age : %s\n",F.enf[plus_age].prenom) ;
    bool b =false ;
    for (int i = 0 ;i<nb_famille ; i++){
        if (F.enf[i].prenom==F.prenom_pere)
            b = 1 ;
    }
    if (b)
        printf("Un enfant de la famille a le meme nom que le pere") ;
    else
        printf("aucune enfant de la famille a le meme nom que le pere") ;
    return 0;
}
