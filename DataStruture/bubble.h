void bubble(int arr[],int size)
{
  int i,j,temp;

for(i=0;i<size-1;++i)
{
    for(j=i+1;j<size;++j)
        if(arr[j]<arr[i])
        {
            temp=arr[j];
            arr[j]=arr[i];
            arr[i]=temp;
        }
}
}
