#include <stdio.h>
#include <string.h>
struct produit{
    char ref[100] ;
    float prix ;
};
int n ;
int RechercheProduit(char ref[],struct produit tab[]){
    for (int i = 0 ; i<n ; i++){
        if (strcmp(tab[i].ref,ref)==0)
            return i ;
    }
    return -1 ;
}

int main()
{
    struct produit tab[100] ;
    
    printf("donner nbre de produit : ") ;
    scanf("%d",&n) ;
    for (int i = 0 ; i<n ; i++){
        printf("donner produit num %d\n",i+1) ; 
        printf("ref : ") ;
        scanf("%s",tab[i].ref) ;
        printf("prix : ") ;
        scanf("%f",&tab[i].prix) ;
    }
    char ref[100] ;
    printf("donner une ref : ") ;
    scanf("%s",ref) ;
    int x =RechercheProduit(ref , tab) ;
    if (x==-1)
        printf("absence du produit") ;
    else 
        printf("Le prix du produit est %.2f | Sa postion : %d",tab[x].prix,x) ;
    return 0;
}
