
class MyException{
  public static void main(String args[]){
      try{
           System.out.println("1st try");
      try{
           System.out.println("going to divide");
           int x=100/0;
         }catch(ArithmeticException e)
         {
           System.out.println(e);
          }
           try{

            int a[]=new int[5];
            a[5]=4;
          System.out.println("other statement"+a[10]);
         }

        catch(ArrayIndexOutOfBoundsException e) 
        {
          System.out.println(e);
        }
        
            System.out.println("other statement");
        
        }catch(Exception e)
        
        {   System.out.println("Exception handeled");
        }
            System.out.println("casual flow of the program");
        }
        
}