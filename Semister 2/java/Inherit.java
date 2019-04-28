class Parent
{
    int x=12;
    float sal=2000; 
}
class child extends Parent {
int y=10;
}

class Inherit extends  child
{
public static void main(String[] args) {

 try{

         Inherit ob1=new Inherit();
         System.out.println("From base class"+ob1.sal);

         System.out.println("From child class"+ob1.y);
         System.out.println("From child class"+ob1.x);

       
     }
catch(ArithmeticException e){System.out.println(e);}  
//rest code of the program   
System.out.println("rest of the code...");  }

}