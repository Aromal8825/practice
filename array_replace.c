// replace a element for an array //
#include<stdio.h>
void main()
{
    int a[10], n, i, new, index;
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
    printf("enter the replace element and index : ");
    scanf("%d %d", &new, &index);
    a[index] = new;
    if(index > n-1)
    {
        printf("invalid index ");
    }
    else
    {
        printf("array after replaing : ");
        for (i = 0; i < n; i++)
        {
            printf("%d ", a[i]);
        }
    }
}
