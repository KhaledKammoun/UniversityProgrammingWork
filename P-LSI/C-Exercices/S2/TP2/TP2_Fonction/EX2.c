#include <stdio.h>
void saisi(int*n){
    bool b = 1 ;
    do{
        b=1 ;
        int t[10]={0} ;
        printf("donner n : ") ;
        scanf("%d",n) ;
        int x = *n ;
        while (x>0){
            t[x%10]++ ;
            if (t[x%10]>1)
                b=0 ;
            x/=10 ;
        }
    }while(b==0) ;
}
int produit(int n1, int n2){
    int som = 1 ;
    bool t[10]={false} ;
    while (n2>0){
        t[n2%10]=true ;
        n2/=10 ;
    }
    while (n1>0){
        if (t[n1%10]!=0){
            som*=(n1%10) ;
            t[n1%10]=false ;//remarque
        }
        n1/=10 ;
    }
    return som ;
}
void multiple(int p){
    if (p%9==0)
        printf("%d est multiple de 9\n",p) ;
    else
        printf("%d est non multiple de 9\n",p) ;
}
int main()
{
    int n1,n2, p ;
    printf("Nombre N*1 : \n") ;
    saisi(&n1) ;
    printf("Nombre N*2 : \n") ;
    saisi(&n2) ;
    p = produit(n1,n2) ;
    multiple(p) ;
    return 0;
}
