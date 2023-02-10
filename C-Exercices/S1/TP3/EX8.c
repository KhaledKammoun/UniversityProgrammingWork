#include <stdio.h>
int main()
{
    for (int i =1 ;i<6;i++)
    {

        for (int j = 0 ;j<((i*2)-1);j++)
        {
            printf("%c",'*') ;
        }
        printf("\n") ;
    }
}
