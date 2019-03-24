#include<stdio.h>
#include<stdlib.h>

int main(){
    int num, exeTime[20],waitTime=0,tat=0;
    int i;
    float awt,atat;
    float sumWT,sumTAT;

    printf("\nEnter the number of process : ");
    scanf("%d",&num);

    for(i=0;i<num;i++){
        printf("\nEnter execution time for process %d : ",i+1);
        scanf("%d",&exeTime[i]);
    }


for(int i=0;i<num;i++){
    for(int j=0;j<num;j++){
        if(exeTime[i]<exeTime[j]){
            int temp = exeTime[i];
            exeTime[i]=exeTime[j];
            exeTime[j]=temp;
        }
    }
}

printf("\nPid \t\t BT \t\t WT \t\t TAT");

for (int i=0;i<num;i++){
    tat=exeTime[i]+waitTime;
    printf("\n%d\t\t%d\t\t%d\t\t%d\n",i,exeTime[i],waitTime,tat);
    sumWT += waitTime;
    sumTAT += tat;
    waitTime += exeTime[i];

}

awt = sumWT/num;
atat= sumTAT/num;
printf("AWT %f ",awt);
printf("ATAT %f ",atat);

}