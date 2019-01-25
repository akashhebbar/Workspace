class emp:
    amt=1.04
    def __init__(self,name,eid,pay):
        self.name=name
        self.eid=eid
        self.pay=pay
    def ramt(self):
        self.pay=int(self.pay*self.amt)
    def display(self):
        print ("First Name ==>",self.name)
        
        print ("Employee ID ==>",self.eid)
        print ("Employee Pay ==>",self.pay)
class dev(emp):
    amt=1.08
    def ramt(self):
        self.pay=int(self.pay*self.amt)
class man(emp):
    amt=1.09
    def ramt(self):
        self.pay=int(self.pay*self.amt)
e1=dev('akash','10001',12000)
e2=man('bhavya','10002',12000)

e1.ramt();
e2.ramt()

e1.display()
e2.display()