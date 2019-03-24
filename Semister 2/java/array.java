import java.util.*;
public class array{
public static void main(String[] args)
{
    Scanner s=new Scanner(System.in);
   String [] val;
   val=new String[4];
   int i;
   int l=4;
   for (i=0;i<l;i++)
   {System.out.println("Enter the name");
    val[i]=s.nextLine();
   }
 
   for(i=0;i<l;i++)
   {
       System.out.println(val[i]);
   }
}
}