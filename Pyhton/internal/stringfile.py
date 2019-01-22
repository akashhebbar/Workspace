while True:
    print("1.open")
    print("2.add")
    print("3.read")
    print("4.cont")
    ch=int(input("Enter the choice"))
    if ch==1:
        a =input("Enter the file name")
        f=open(a,'w')
        print("file created")
    elif ch==2:
        b=input("Enter some txt")
        f.write(b)
        print("write done")
    elif ch==3:
        f=open(a,'r')
        c=f.read()
        print(c)
        f.close()
    elif ch==4:
        f=open(a,'r')
        c=f.read()
        print("split",c.split())
        print("totla",len(c.split()))
    elif ch==5:
        f=open(a,'r')
        c=f.read()
        n=input("Enter new file name")
        g=open(n,'w')
        g.write(c.upper())
        g.close()
        g=open(n,'r')
        c=g.read()
        print(c)

