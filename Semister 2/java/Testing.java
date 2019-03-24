class Testing{

	int a; //instance var
	static int b=30;

	{
		this.a=40;
	}
	public static void main(String[] args){
		
		System.out.println("Hello world");
		Testing obj = new Testing();
		System.out.println("Hello world" + obj.a);
		System.out.println("Hello world" + b);
		System.out.println("Hello world" + Testing.b);
		
		

	
	}
	}