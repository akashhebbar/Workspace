#include<stdio.h>
#include <ctype.h>
int stack[50];
int top=-1;
void push(int x)
{
  stack[++top]= x;
}
int pop()
{
  return stack[top--];
}
int main()
{
char exap[50];
char *e;
int n1,n2,n3,num;
printf("Enter the expression");
scanf("%s",exap);
e=exap;
while(*e!='\0')
{
  if(isdigit(*e))
  {
          num = *e - 48;
          push(num);

  }
  else
  {

    n1=pop();
    n2=pop();
  switch(*e)
  {
    case '+':
          {
              n3=n1+n2;
              break;
          }
    case '-':
            {
              n3=n2-n1;
              break;

            }
    case '*':
              {
                n3=n1*n2;
                break;
              }
    case '/':
    {
      n3=n2/n1;
      break;
      }

  }
  push(n3);





}e++;


  }
  printf("\nThe result of expression %s  =  %d\n\n",exap,pop());
  return 0;
}
