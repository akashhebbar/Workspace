#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define max 10
char stack[max][80];
int top =-1,size;


    int push(char data[50])
    {
        if(top==size-1)
        
            printf("overflow");
else
{top=top+1;
    strcpy(stack[top],data);
    printf("pushed data: %s",data);

}
    }
    int pop(char data[50])
    {
        if(top==-1)
        printf("undeflow");
        else
        {
            strcpy(data,stack[top]);
            printf("data %s",data);
            top=top-1;
            return(1);

        }
        }
        
void display(){
    if (top == -1)
        printf("\nStack is underflow\n");
    printf("\nStack element are : \n");
    for(int i=top;i>=0;i--)
    {
        printf("%s\n",stack[i]);
    }
}
    
    int main()
{stack[max][80];
    char nm[80];
    int ch;
    printf("Enter the size of stack");
    scanf("%d",&size);

    while(1)
    {
        printf("stack");
        printf("1.push");
        printf("2.pop");
        printf("display");

        printf("Enter the choice");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
            printf("Enter the string:");
            scanf("%s",nm);
            push(nm);
            break;
            case 2:
                pop(nm);
                break;
            case 3:display(nm);
            break;

        }
    }return 0;
}
    