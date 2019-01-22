t1=('hell00000000000000000000000o','world','hh','f','h','s','q')
t2=('xxxxxx','yyyyyyyyyyyyy')
while True:
    print("1.contact")
    print("2.craete")
    ch=int(input("Enter the choice"))
    if ch==1:
        print(t1+t2)
    if ch==2:
        t3=()
    if ch==3:
        print(t1*2)
    if ch==4:
        print(t1[1:3])
    if ch==5:
        print(max(t1))
    if ch==6:
        del t1
    if ch==7:
            for i in t1:
                print(i)