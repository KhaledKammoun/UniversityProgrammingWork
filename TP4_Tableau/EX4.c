#include <stdio.h>
float moyenne(int n , float *t)
{
    float somme=0.0;
    for (int i = 0 ;i<n ; i++)
        somme+=t[i] ;
    return (somme/n) ;
}
float maximum(int n , float *t)
{
    float Max=t[0] ;
    for (int i = 1 ; i<n ;i++){
        if (Max<=t[i])
            Max=t[i] ;
    }
    return Max ;
}
float minimum(int n , float *t)
{
    float Min=t[0] ;
    for (int i = 1 ; i<n ;i++){
        if (Min>=t[i])
            Min=t[i] ;
    }
    return Min ;
}
int main()
{
    int n ;
    float t[30]={0.0};
    printf("donner la taille du tableau : ") ;
    scanf("%d",&n) ;
    for (int i = 0 ;i<n ; i++){
        do{
            scanf("%f",&t[i]) ;
        }while(t[i]<1 || t[i]>20) ;
    }
    //affichage
    for (int i = 0 ;i<n ; i++)
        printf("%f ",t[i]) ;
    float moy=moyenne(n,t) ;
    float Max=maximum(n,t) ;
    float Min=minimum(n,t) ;
    return 0;
}
