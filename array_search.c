// search for a given element in array //
#include<stdio.h>
void main()
{
    int a[10], n, i, search, found;
    printf("enter number of elements : ");
    scanf("%d", &n);
    if(n < 1) 
    {
        printf("invalid number");
        return;
    }
    printf("enter %d numbers : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    printf("enter the search element : ");
    scanf("%d", &search);
    for (i = 0; i < n; i++)
    {
        if(search == a[i])
        {
            found = 1;
            break;
        }
    }
    if(found == 1)
    {
        printf("%d found at index %d ", search, i);
    }
    else
    {
        printf("%d not found ", search);
    }
}
