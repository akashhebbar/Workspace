class FinallyBlock{
 public static void main(String args[]){
   try{

     int data=100/0;
     System.out.println(data);
    
    }
    catch(NullPointerException e)
       {
         System.out.println(e);
      } 
    finally {

      System.out.println("------finally block----");
}
    System.out.println("code");
  }}
