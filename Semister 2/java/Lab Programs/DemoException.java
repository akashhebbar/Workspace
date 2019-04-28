

class InvalidException extends Exception{
    InvalidException(String s)
    {
        super(s);
    }
}
class DemoException{   
    static void validate(int age)throws InvalidException
    {
        if(age<18)
        {
            throw new InvalidException("cant vote");
        }
            else
            {
System.out.println("you can vote");
            }
        }
    
    public static void main(String[] args)
    {
        try{

            validate(10);
        
        }
        catch(Exception e)
        {
            System.out.println("Exception occured");
        }

    }
}