ch=int(input("Enter the choice "))
while True:
    if ch==1:
        name=input("Enter the file name")
        dname=input("Enter the desitnation file name")
    elif ch==2:
        try:
            a=open(name,"w")
        except Exception:
            print("cant create a file")
