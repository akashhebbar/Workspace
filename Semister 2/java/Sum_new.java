import java.util.Scanner;
public class Sum_new
{
    public static void main(String[] args) 
    {
        int n,i, sum = 0;
        float average;
        String n1,n2,n3;
        String  s1;
        Scanner s = new Scanner(System.in);
        Scanner in = new Scanner(System.in);
        System.out.print("Enter no. of elements you want in array:");
        n = s.nextInt();
        System.out.println("Enter a string");
      s1 = in.nextLine();
        int a[] = new int[n];
        System.out.println("Enter all the elements:");
        for( i = 0; i < n ; i++)
        {
            a[i] = s.nextInt();
            sum = sum + a[i];
        }
        System.out.println(s1);
        System.out.println("Sum:"+sum);
        average = (float)sum / n;
        System.out.println("Average:"+average);
    }
}