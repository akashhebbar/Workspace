import java.io.*;

public class oppcar
{
    public int cost=10;
    public String model;
    private int  speed=180;
public void setmodel(String model)
{
this.model=model;
}
public String getmodel()
{
return this.model;
}
public static void main(String[] args)
{
    oppcar ob1=new oppcar();
    System.out.println(ob1.cost);
    System.out.println(ob1.speed);
    ob1.setmodel("gtr");
    System.out.println( ob1.getmodel());
}



} 

