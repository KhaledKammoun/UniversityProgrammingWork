#include <stdio.h>

//exemple1 n = 5 | t : 1 1 2 2 1 ==> 1 2
// 2 : n = 5 | t : 1 2 3 4 5 ==> 1 2 3 4 5

void saisie (int *n , int *t)
{
    do{
        scanf("%d",n) ;
    }while (*n>50 || *n<1) ;
    for (int i = 0 ;i<*n; i++) //Saisie
    {
        int occ  ;
        do
        {
            occ=0 ;
            scanf("%d",&t[i]) ;
            for (int j = 0 ; j<(i+1) ; j++)
            {
                if (t[i]==t[j])
                    occ++ ;
            }
        }while (occ>3 || t[i]==0) ;
    }
}
void decalage(int *n , int *t){
    int dec= (*n-1) , i =0;
    while (i<*n && t[i+1]!=0)
    {
        int j=dec ; // dernier element different de 0
        while (t[i]!=t[j] && j>(i+1)){
            j-- ;
        }
        if (t[i]==t[j])
        {
            for (int k = j ; k<dec ; k++) //Décalage
                t[k]=t[k+1] ;
            t[dec]=0 ;
            dec-- ;
        }
        else
            i++ ;
    }
}
void affichage(int *n , int *t){
    for (int i = 0 ;i<*n ;i++) //affichage
    {
        if (t[i]!=0)
            printf("%d ",t[i]) ;
    }
}
int main()
{
    int n ;
    int t[100]={0} ;//initialiser le tableau à 0

    saisie(&n,t) ;// &n : adresse de n

    decalage(&n,t) ;

    affichage(&n , t) ;
    return 0;
}
