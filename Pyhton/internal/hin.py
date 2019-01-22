class student:
    def __init__(self,name,usn,age=0):
        self.name=name
        self.usn=usn
        self.name=name
        self.age=age
    def getdata(self):
        self.usn=input("Enter the usn")
        self.name=input("Enter the name")
        self.age=input("Enter the age")
    def display(self):
        print("usn==:",self.usn)
        print("name=:",self.name)
        print("age==:",self.age)
class pgstudent(student):
    def __init__(self,sem=0,course=0):
        self.sem=sem
        self.course=course
    def getpgdata(self):
        self.sem=input("Enter the sem")
        self.course=input("Enter the course")
    def pgdisplay(self):
        print("sem=",self.sem)
        print("course=",self.course)
class ugstudent(student):
    def __init__(self,fee=0,roll=0):
        self.fee=fee
        self.roll=roll
    def getugdata(self):
        self.fee=input("Enter feee")
        self.roll=input("Enter the rooll")
    def ugdisplay(self):
        print("feee=",self.fee)
        print("rolll=",self.roll)
        
pgg=pgstudent()
ugg=ugstudent()
while True:
    print("1.pg")
    print("2.ug")
    ch=int(input("Enter the chcoice "))
    if ch==1:
        pgg.getdata()
        pgg.getpgdata()
        pgg.display()
        pgg.pgdisplay()


