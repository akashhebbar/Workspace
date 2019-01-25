while True:
    print("1.crrate")
    alist=[2]
    alist1=[3,5,6]
    ch=int(input("Ente rthe choice"))
    if ch==1:
        n=int(input("Enter the size"))
        for i in range(0,n):
                item=int(input("Enter the elenmts"))
                alist.append(item)
        print(alist)
    elif ch==2:
        for i in range(0,3):
            print(alist)
    elif ch==3:
        print("lenfgt",len(alist))
    elif ch==4:
        print("join",alist1+alist)
    elif ch==5:
        print(alist1[0:1])
    elif ch==6:
        print(alist1[::-1])
    elif ch==7:
        z=int(input("ENtert the vale"))
        print(alist1[0:z])
    elif ch==8:
        print(alist1.__sizeof__)
    elif ch==9:
        print(alist1)
        print(alist1)
    elif ch==10:
        print(alist1.remove(3))
        print(alist1)