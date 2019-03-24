class method
{ 
    

    int l,b;



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

class rect
{
    int l,b;
    rect(String q,int w)
    {
        q=0;
        b=20;
    }
    rect ()
    {
        l=b=0;
    }
    
   


    int area()
    {
            return (l*b);
    
    }
    int area(int a)
    {
            return (a*a);
    }
    int area2(String a, int b)
    {
            a="akash";
            return(b);
    }


}


class overload
{ 
    public static void main(String[] args)
{
    int area1;
    method r1=new method();

        area1=r1.area();
        System.out.println("method overload");
        System.out.println("lenght="+area1);
        area1=r1.area(5);
        System.out.println("area of square"+area1);
        area1=r1.area(5,5);
        System.out.println(area1);





        System.out.println("constructer overload");
        rect myrect=new rect();
        area1=myrect.area();
        System.out.println(area1);

        rect myrect1=new rect("akaa",4);
        area1=myrect1.area();
        System.out.println(area1);
}

}