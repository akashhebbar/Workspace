#include<conio.h>
#include <stdlib.h>
#include<stdio.h>
typedef struct BST{
  int data;
  struct node *left,*right;
}node;
node *newnode, *root;

void insert(node* ,node*);
void postorder(node*);
node *getnode();

void main()
{int ch;
  int key;
root=NULL;

  printf("bst");
while(1)
{
  printf("\n1.Create");
  printf("\n2. Traverse in Inorder");
  printf("\n3. Traverse in Preorder");
  printf("\n4. Traverse in Postorder");
  printf("\n5. Exit\n");
  printf("\nEnter your choice :");
  scanf("%d", &ch);

  switch (ch)
{
  case 1:  newnode = getnode();
    printf("\nEnter The Element ");
    scanf("%d", &newnode->data);
    if (root == NULL) /* Tree is not Created */
        root = newnode;
    else
        insert(root, newnode);
break;
  case 4:postorder(root);




break;
        }




}

}
node* getnode()
{
  node*temp;
  temp=(node*)malloc(sizeof(node*));
  temp->left=NULL;
  temp->right=NULL;
  return temp;

}
void insert(node *root, node *newnode)
{
  if(newnode->data < root-> data)
{

  if(root->left==NULL)

    root->left=newnode;
    else
    insert(root->left,newnode);
    }
}
void postorder(node*temp)
{
  if(temp!=NULL)
  {
    postorder(temp->left);

    postorder(temp->right);
    printf("data-->%d",temp->data);
  }
}
