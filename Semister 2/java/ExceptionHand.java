class InvalidException extends Exception{
    InvalidException(string s)
    {

    }
}
class ExceptionHand{
    public static void main(String[] args)
    {
     static   void valid(int age)throws InvalidException{
        if(age>18)
        {
            throw new InvalidException()
        }
        }
    }

  }
