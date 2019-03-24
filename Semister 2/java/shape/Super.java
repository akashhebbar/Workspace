class Parent
{
    int a=10;
    int b=20;
}
class Super extends Parent
{int a=50;
    int b=50;
void add(int a,int b)
{
  System.out.println("sum"+(this.a+this.b));
  System.out.println(super.a+super.b);

System.out.println(a+b);
}
public static void main(String[] args)
{
Super ob1=new Super();
ob1.add(100,100);
}


}
