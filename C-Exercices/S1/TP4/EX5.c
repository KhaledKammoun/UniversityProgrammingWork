#include <stdio.h>

void Remplir(int n,int *t )
{
    for (int i = 0 ;i<n ; i++){
        do{
            scanf("%d",&t[i]) ;
        }while(t[i]<=0) ;
    }
}

void Afficher(int *n , int *t)
{
    for (int i = 0 ; i<*n ; i++)
        printf("%d ",t[i]) ;
}
bool cherche(int x, int ind,int *t)
{
    for (int i = 0 ;i<ind ; i++){
        if (t[i]==x)
            return true ;
    }
    return false ;
}

void Contact(int *ind , int n , int m,int *t ,int *t1, int *t2)
{
    *ind=0 ;
    for (int i = 0 ;i<n ; i++){
        if (cherche(t1[i],*ind,t)==false){

            t[*ind]=t1[i] ;
            (*ind)++ ;

        }
    }
    for (int i = 0 ;i<m ; i++){
        if (cherche(t2[i],*ind,t)==false){

            t[*ind]=t2[i] ;
            (*ind)++ ;

        }
    }
}

int main()
{
    int d1,d2,ind=0;
    do{
        printf("donner d1 : ") ;
        scanf("%d",&d1) ;
        printf("donner d2 : ") ;
        scanf("%d",&d2) ;

    }while(2>=d1 || d1>=d2 || d2>=20) ;

    int c[d1+d2]={0},a[d1]={0},b[d2]={0} ;
    printf("donner les element de A : ") ;
    Remplir(d1,a) ;
    printf("donner les element de B : ") ;
    Remplir(d2,b) ;
    Contact(&ind,d1,d2,c,a,b) ;
    Afficher(&ind,c) ;
    return 0;
}
