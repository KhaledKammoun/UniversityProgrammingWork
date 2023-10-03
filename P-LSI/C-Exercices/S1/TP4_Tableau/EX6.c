#include <stdio.h>

void saisie(int *n)
{
    do{
        scanf("%d",n) ;
    }while(*n<0 || *n>100) ;
}
void remplir(int n , int *t)
{
    for (int i =0 ;i<n ; i++)
        scanf("%d",&t[i]) ;
}
void tri_selection(int n , int *t)
{
    for (int i = 0 ;i<n ;i++)
    {
        int Min=t[i],ind=i ;
        for (int j=i+1 ; j<n ;j++){
            if (Min>t[j]){
                Min=t[j] ;
                ind=j ;
            }
        }
        int a=t[i] ;
        t[i]=t[ind] ;
        t[ind]=a ;
    }

}
int main()
{
    int n ,t[100]={0} ;
    saisie(&n);
    remplir(n,t) ;
    tri_selection(n,t) ;
    for (int i = 0 ;i<n ; i++)
        printf("%d  ",t[i]) ;
    return 0;
}
