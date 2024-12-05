// array insertion //
#include <stdio.h>
#include <stdlib.h>
void main()
{
    int *arr, n, i, new, pos;
    printf(" enter number of elements : ");
    scanf("%d", &n);
    arr = (int *)malloc(n * sizeof(int));
    printf(" enter %d numbers : ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf(" enter a new element : ");
    scanf("%d", &new);
    printf(" enter the position : ");
    scanf("%d", &pos);
    if (pos > n + 1 || pos <= 0)
    {
        printf(" invalid position ");
    }
    else
    {
        n += 1;                                            
        for (i = n - 2; i >= pos - 1; i--)
        {
            arr[i + 1] = arr[i];
        }
        arr[pos - 1] = new;
        printf(" array after insertion : ");
        for (i = 0; i < n; i++)
        {
            printf("%d ", arr[i]);
        }
        free(arr);
    }
}
