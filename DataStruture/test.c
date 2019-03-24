#include<stdio.h>
void main(){
  int i = 10;
  int *iptr;
  iptr = & i;
  char c = 'c';
  char *cptr = &c;
  float f = 1.2;
  float *fptr = &f;
  printf("size of int [%d] and itptr [%d]", sizeof(i), sizeof(iptr));
  printf("\nsize of char [%d] and ctptr [%d]", sizeof(i), sizeof(iptr));
  printf("\nsize of float [%d] and ftptr [%d]", sizeof(i), sizeof(iptr));


  printf("\naddress of i %lu ",&i);
  printf("\naddress of c %lu ",&c);
  printf("\naddress of f %lu ",&f);

  printf("\naddress of iptr %u ", iptr);
  printf("\naddress of cptr %u ", cptr);
  printf("\naddress of fptr %u ", fptr);

  // printf("\nvalue using pointer of i %d ",*i );
  
}
