#include <stdio.h>
int prem_carr(int n){
    if (n == 1)
        return 1;
    else
        return n*n + prem_carr(n-1);
}
int main(){
    int n ;
    do{
        printf("Donner un entier n positif : ") ;
        scanf("%d",&n) ;
    }while (n<=0) ;
    printf("La somme de x est : %d",prem_carr(n)) ;
}