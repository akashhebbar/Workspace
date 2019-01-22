s1={1,2,3,8,9,"hello"}
s2={'hello','world',8}
while True:
 print("1.union")
 ch=int(input("enter the number"))
 if ch==1:
    print(s1.union(s2)) 
 if ch==2:
    print(s1.intersection(s2))
 if ch==3:
    print(s1.add(2222222222))
    print(s1)
 if ch==4:
     print(s1.pop())
     print(s1)
 if ch==5:
     print(s1-s2)
 if ch==6:
     print(s1^s2)
 if ch==7:
     print(s1.__contains__(10000))
      
       