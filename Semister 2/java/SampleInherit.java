class Travel
{
    int x=12;
    float sal=2000; 
    public void move()
    {
        System.out.println("Travel by bus");
    }
}
class car extends Travel {
    int y=10;
    public void move1()
    {
        System.out.println("travel by car");
        super.move();
    }
    }

class SampleInherit extends  car
{
public static void main(String[] args) {

 try{

         SampleInherit ob1=new SampleInherit();
         ob1.move();
         ob1.move1();

        //  System.out.println("From child class"+ob1.y);
        //  System.out.println("From child class"+ob1.x);

       
     }
catch(ArithmeticException e){System.out.println(e);}  
//rest code of the program   
System.out.println("rest of the code...");  }

}