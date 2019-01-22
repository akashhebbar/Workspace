class op:
    def __init__(self):
        self.alist=[]
    def get(self):
        n=int(input("Enter the size"))
        for i in range(0,n):
            item=int(input("Enter the item"))
            self.alist.append(item)
        return self.alist
    def __add__(self,other):
        new=[]
        for i in range(0,len(self.alist)):
            new.append(self.alist[i]+other.alist[i])
        return new
    def __sub__(self,other):
        new=[]
        for i in range(0,len(self.alist)):
            new.append(self.alist[i] - other.alist[i])
        return new
    def __mul__(self,other):
        new=[]
        for i in range(0,len(self.alist)):
            new.append(self.alist[i] * other.alist[i])
        return new
    def __trudiv__(self,other):
        new=[]
        for i in range(0,len(self.alist)):
            new.append(self.alist[i] / other.alist[i])
        return new
    def __floordiv__(self,other):
        new=[]
        for i in range(0,len(self.alist)):
            new.append(self.alist[i] // other.alist[i])
        return new




ov1=op()
ov2=op()

ov1.get()
print(ov1.alist)
ov2.get()
print(ov2.alist)
while True:
    ch=int(input("Enter the choice"))
    if ch==1:
        print(ov1+ov2)
    elif ch==2:
        print(ov1-ov2)
    elif ch==3:
        print(ov1*ov2)
    elif ch==4:
        print(ov1/ov2)
    elif ch==5:
        print(ov1//ov2)
