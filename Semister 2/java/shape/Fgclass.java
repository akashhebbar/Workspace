class Fgclass
{
public static void main(String[] args)
{

Fgclass f=new Fgclass();
int t=0;
System.gc();
f.finalize();



}
public void finalize()
{
    System.out.println("gc");
}



}