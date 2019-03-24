class rect
{ 
    int s,j;
    
rect(int q,int w)
{
    l=q;
    b=w;
}
rect ()
{
    l=b=0;
}

rect(int h)
{
    s=0;
}
    int l,b;

void rectange()
{
    l=0;
    b=0;
}
void rectange(int m)
{
        l=m;
        b=m;
}
void rectange(int m, int n)
{
        l=m;
        b=n;
}

int area()
{
        return (l*b);

}
int area(int a)
{
        return (a*a);
}
int area(int a, int b)
{
        return (a*b);
}}




class shape
{ 
    public static void main(String[] args)
{
    int area1;
    rect r1=new rect();

        area1=r1.area();
        System.out.println("method overload");
        System.out.println(area1);
        area1=r1.area(5);
        System.out.println(area1);
        area1=r1.area(5,5);
        System.out.println(area1);


        System.out.println("constructer overload");
        rect myrect=new rect();
        area1=myrect.area();
        System.out.println(area1);

        rect myrect1=new rect(9,4);
        area1=myrect1.area();
        System.out.println(area1);
}

}