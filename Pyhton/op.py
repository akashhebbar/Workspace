class op:
    def __init__(self):
        self.alist=[]
    def get(self):
        n=int(input("ENter the size"))
        for i in range(0,n):
            item=int(input("Enter the item"))
            self.alist.append(item)
        return self.alist
    def __add__(self,other):
        new=[]
        for i in range(0,len(self.alist)):
            new.append( self.alist[i]+other.alist[i])
        return new
obj1=op()
obj2=op()
obj1.get()
obj2.get()

while True:
    ch=int(input("Enter the choice"))
    if ch==1:
        print(obj1+obj2)

