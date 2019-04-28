import java.io.Console;
interface Rectangle
{
double area(float x, float y);


}
interface Triangle
{
    double tri(float x,float y); 
}
class DemoInterface implements Rectangle,Triangle
{
    
    
      public  double tri(float x,float y)
      {
          return(x*y);
      } 
      public double area(float x,float y)
      {
        return(x*y);

      }
      public static void main(String[] args)
      {
        DemoInterface a=new DemoInterface();
       
        Console c=System.console();

        System.out.println("Enter the width and height");
        int w=Integer.parseInt(co.readLine());
        int h=Integer.parseInt(co.readLine());
        System.out.println("area="+a.tri(w,h));
        System.out.println("Enter the length and breadth");
        int l=Integer.parseInt(co.readLine());
        int b=Integer.parseInt(co.readLine());
        System.out.println("area="+a.area(l,b));
      }

    }

