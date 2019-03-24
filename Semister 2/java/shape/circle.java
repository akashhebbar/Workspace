 package shape;
public class circle
{
    private double rad;
    public void setcircle(double radius)
    {
        rad=radius;
    }
    public void area()
    {
        double area=(0.5)*3.14*rad*rad;
        System.out.println("area"+area);
    }
}