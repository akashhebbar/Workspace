import java.io.*;
import java.util.Scanner;
 class Overload
{
int x;
String s;
double d;

Overload()
{
    x=0;
}
Overload(int a)
{
 x=a;
 System.out.println("with parameter"+x);
}
Overload(int a,double b)
{
    d=b;
    d=b;
    System.out.println("With diffrent parameter"+x);
}
public int add(int g)
{
    int x=g;
    System.out.println(x);
    return(x+x);

}
public int add(int n1,int n2)
{
    return(n1*n2);
}

}

public class Overloading{
    public static void main(String args[])
    {   int q=5;
      
        Scanner in=new Scanner(System.in);
        while(q!=4)
        {
        System.out.println("1.Construct Overload");
        System.out.println("2.method Overload");
        System.out.println("Enter the choice");
        q=in.nextInt();
        switch(q)
        {
            case 1:
            Overload ob1=new Overload();
            Overload ob2=new Overload(10);
            Overload ob3=new Overload(10,10);
            break;
            
            case 2:
                System.out.println("Enter the number");
                int num1=in.nextInt();
                Overload ov6=new Overload();
                System.out.println(ov6.add(num1));
        }
    }
}
}