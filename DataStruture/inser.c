#include<stdio.h>
#include "in.h"

176
void insertion(int[]
);
int main() {
    int arr_sort[MAX_SIZE], i;

    printf("Simple Insertion Sort Example - Array and Functions\n");
    printf("\nEnter %d Elements for Sorting\n", MAX_SIZE);
    for (i = 0; i < MAX_SIZE; i++)
        scanf("%d", &arr_sort[i]);

    printf("\nYour Data   :");
    for (i = 0; i < MAX_SIZE; i++) {
        printf("\t%d", arr_sort[i]);
    }

    insertion(arr_sort);

}
