#include <stdio.h>
#include <malloc.h>
int som(int*tab , int ind){
    if (*(tab+ind)=='\0')
        return 0 ;
    else {
        if (*(tab+ind)>0)
            return *(tab+ind) + som(tab,ind+1) ;
        else 
            return som(tab, ind+1) ;
    }
}
int main(){
    int *tab,i=0,n ;
    printf("Donner n : ") ;
    scanf("%d",&n) ;
    tab = (int*)malloc(sizeof(int)*(n)) ;
    printf("Donner les entiers du tableau : \n") ;
    for (i ; i<n ; i++){
        printf("N%d = ",i) ;
        scanf("%d",tab+i) ;
    }
    *(tab+i)='\0' ;
    int ind ; 
    printf("Donner l'indice de debut : ");
    scanf("%d",&ind) ;
    printf("La somme est : %d",som(tab,ind)) ;
}