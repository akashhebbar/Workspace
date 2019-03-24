class emp
{
    int salary=12000;
}

class TestInheritance extends  emp
{
public static void main(String[] args) {

    try{
         TestInheritance ob1=new TestInheritance();
 System.out.println(ob1.salary);   
}catch(ArithmeticException e){System.out.println(e);}  
//rest code of the program   
System.out.println("rest of the code...");  }

}