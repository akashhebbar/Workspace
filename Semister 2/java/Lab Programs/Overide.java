class Travel
{
  
    public void move()
    {
        System.out.println("Travel by bus");
    }
}
class car extends Travel {
   
    public void move1()
    {
        int x=10;
        System.out.println(x);
        System.out.println("travel by car");
         super.move();
    }
    }

class Overide extends  car
{
public static void main(String[] args) {

 try{

    Overide ob1=new Overide();
    Overide ob2=new Overide();
     ob1=new car();
        
         ob1.move1();

        //ob2.move();
       
        //  System.out.println("From child class"+ob1.y);
        //  System.out.println("From child class"+ob1.x);

       
     }
catch(ArithmeticException e)
{
    System.out.println(e);
}  
//rest code of the program   
System.out.println("rest of the code...");  }

}