class emp:
    ramt=1.04
    
    def __init__(self,name=0,empid=0,pay=0):
        self.name=name
        self.empid=empid
        self.pay=pay
    def amt(self):
        self.pay=int(self.pay*self.ramt)
    def disp(self):
        print("name=",self.name)
        print("empid=",self.empid)
        print("pay amount")
        return self.pay
        
class dev(emp):
    ramt=1.06
    def amt(self):
        self.pay=int(self.pay*self.ramt)
class man(emp):
    ramt=1.08
    def amt(self):
        self.pay=int(self.pay*self.ramt)
e1=man('bhavya',10001,15000)
e2=dev('akash',10003,13000)

print(e1.pay)
print(e2.pay)
e1.amt()
e2.amt()
print(e1.disp())
print(e2.disp())