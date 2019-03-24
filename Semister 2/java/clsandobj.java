class Obj{
    int x;
    int y;
    int result;
    public void perform()
    {
        result=x+y;
    }
}
public  class clsandobj{



public static void main(String[] args)
{
    Obj ob=new Obj();
ob.x=10;
ob.y=20;
ob.perform();
    System.out.println(ob.result);
}}