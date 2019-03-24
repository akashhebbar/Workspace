#include<stdio.h>
#include "in.h"
#include "selection.h"

#define MAX 20

int main(){

      int list[50];
      int i, size;
      int ch;

      printf("Enter total number of elements:");
      scanf("%d", &size);
      printf("Enter the elements:\n");
      for(i = 0; i < size; i++)
      {
           scanf("%d", &list[i]);
      }

    while (1) {

        printf("1-insertion sort\n 2-selection \n");
      printf("enter choice\n");
      scanf("%d",&ch );

      switch (ch) {
        case 1:
          insertion(list);
          break;
        case 2:
            exchang(list, size);

        printf("Sorted array is...\n");
        for (i = 0; i < size; i++)
        {
            printf("%d\n", list[i]);
        }
        break;

      }
    }

     return 0;
}
