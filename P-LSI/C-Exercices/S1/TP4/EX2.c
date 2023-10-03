#include <stdio.h>
void fusion(int *t,int *a,int *b, int s , int n , int m)
{

    int j=0 , k=0 , i=0;
    while(j<n && k <m)
    {

        if (a[j]>b[k] )
        {
            t[i]=b[k] ;
            k++ ;
        }
        else
        {
            t[i]=a[j] ;
            j++ ;
        }
        i++ ;
    }
    while(j<n)
    {
        t[i]=a[j] ;
        i++;
        j++;
    }
    while(k<m)
    {
        t[i]=b[k] ;
        i++ ;
        k++ ;
    }

}
int main()
{
    int n ,m ;
    scanf("%d %d",&n,&m) ;
    int a[n]={0},b[m]={0} ;
    scanf("%d",&a[0]) ;
    for (int i = 1 ; i<n ; i++)
    {
        do{
            scanf("%d",&a[i]) ;
        }while (a[i]<a[i-1]) ;
    }
    scanf("%d",&b[0]) ;
    for (int i = 1 ; i<m ; i++)
    {
        do{
            scanf("%d",&b[i]) ;
        }while (b[i]<b[i-1]) ;
    }
    int s =n+m ;
    int t[s]={0} ;
    fusion(t,a,b,s,n,m) ;
    for (int i = 0 ;i<s ; i++)
        printf("%d  ",t[i]) ;
    return 0;
}
