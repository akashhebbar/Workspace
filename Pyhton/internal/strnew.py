
d1={'name':'123','age':'23','car':'mustang'}
d2={'name':'arun','sem':'firt'}

while True:
    print("1.add")
    print("2.rep")
    print("3.slice")
    print("4.just slixce")
    print("5.member")
    print("7.length")
    print("8.white")
    print("9.print")
    print("10.sub")
   
    ch=int(input("Enter the choice"))
    if ch==1:
        print(d1.values())
    elif ch==2:
        print(d1.keys())
    elif ch==3:
        print(d1.items())
    elif ch==4:
        k=input("enter key")
        v=input("values")
        d1[k]=v
        print()
    elif ch==5:
        d=input("Enter the key to deleete")
        del d1[d]
        print(d1)
    elif ch==6:
        d1.clear()
        print(d1)
    elif ch==7:
        k=int(input("Enter the key"))
        print(k in d1)
    
   
        

