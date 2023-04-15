#include <iostream>

using namespace std;
int somchif (int n ){
    int som = 0 ;
    while (n!=0){
        som+=n%10 ;
        n/=10 ;
    }
    return som ;
}
int inverse(int n){
    int inv =0 ;
    while (n!=0){
        inv = inv*10 + n%10 ;
        n/=10 ;
    }
    return inv ;
}
int main()
{
    int n ;
    do{
        printf("donner n : ") ;
        scanf("%d",&n) ;

    }while (n<5284) ;
    int som = 0 ;
    som = somchif(n) ;
    printf(" La somme des chiffres du nombre n est %d\n",som) ;
    int inv = inverse(n) ;
    printf("L'inverse du nombre n est %d",inv) ;
    return 0;
}
