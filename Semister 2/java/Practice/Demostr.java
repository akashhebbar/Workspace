import java.io.*;
import java.util.Scanner;
class Demostr
{
    int capacity;
    int sc;
    String str;
    StringBuffer s;

void find_cap(StringBuffer s)
{
    capacity=s.capacity();

}

void rev_str(StringBuffer s)
{
   StringBuffer str1;
   str1=s.reverse();
   System.out.println(str1);
}

public static void main(String[] args)
{
    Scanner in=new Scanner(System.in);
    Demostr s=new Demostr();
    Console co=System.console();
    int q=5;
    while(q!=4)
    {
        System.out.println("1.String Methods");
        System.out.println("2.StringBuffer Methods");
        System.out.println("Enter the choice");
        q=in.nextInt();
            switch(q)
            {
                case 1:
                    System.out.println("Enter the string");
                    StringBuffer str=new StringBuffer(co.readLine());
                    s.find_cap(str);
                    System.out.println(s.capacity);
                    s.rev_str(str);
                    break;
 //System.out.println(s.reverse);
                case 2:
                    StringBuffer b1=new StringBuffer();
                    System.out.println("String Append ="+b1.append("hello appended"));

                    break;
            }
    }

}

}

 