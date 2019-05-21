#include<stdio.h>
#include<stdlib.h>

void main()
{
        int num,et[20],at[20],ct=0,wt[20],tat[20];
        int i,temp=0;
        float awt,atat;
        float sumwt,sumtat;

        printf("\nEnter the number of process");
        scanf("%d",&num);

        for(i=0;i<num;i++)
        {
            printf("\nENter the burst time for process %d",i+1);
            scanf("%d",&et[i]);

        }
        for(i=0;i<num;i++)
        {
            printf("/nEnter the arival time for process %d",i+1);
            scanf("%d",&at[i]);

        }
        wt[0]=0;
        for(i=1;i<num;i++)
        {
            temp=temp+et[i-1];
            wt[i]=temp-at[i];
            sumwt=sumwt+wt[i];
        }
        printf("\npid \t at \t bt \t ct \t wt \t tat");
        for(i=0;i<num;i++)
        {
             ct+=et[i];
            tat[i]=ct-at[i];
            sumtat=sumtat+tat[i];
        printf("\n%d \t %d \t %d \t %d \t %d \t %d\n",i+1,at[i],et[i],ct,wt[i],tat[i]);
        }
    awt=sumwt/num;
    atat=sumtat/num;
    printf("\nAvergae turn arunnd time %f:",atat);
    printf("\nAverage waiting time : %f",awt);
    printf("\n");



}