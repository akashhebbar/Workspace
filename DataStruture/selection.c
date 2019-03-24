#include <stdio.h>
#include "selection.h"
int findmax(int b[10], int k);
void exchang(int b[10], int k);
void main()
{
    int array[10];
    int i, j, n, temp;

    printf("Enter the value of n \n");
    scanf("%d", &n);
    printf("Enter the elements one by one \n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }
    printf("Input array elements \n");
    for (i = 0; i < n ; i++)
    {
        printf("%d\n", array[i]);
    }
    /*  Selection sorting begins */
    exchang(array, n);
    printf("Sorted array is...\n");
    for (i = 0; i < n; i++)
    {
        printf("%d\n", array[i]);
    }
}
/*  function to find the maximum value */
