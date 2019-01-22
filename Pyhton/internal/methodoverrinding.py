class emp:
    ramt=1.04
    def __init__(self,first,empid,pay):
        self.first=first
        self.empid=empid
        self.pay=pay
    def amt(self):
        self.pay =  int(self.pay * self.ramt)
    def disp(self):
        print("first",self.first)
        print("empid",self.empid)
        print("pay",self.pay)
        
class dev(emp):
    ramt=1.06
    def amt(self):
        self.pay =  int(self.pay * self.ramt)
class mgr(emp):
    ramt=1.09
    def amt(self):
        self.pay =  int(self.pay * self.ramt) 
e2=mgr('bhavya',1002,10000)
e1=dev('akash',1001,10000)


print(e1.pay)
print(e2.pay)

e1.amt()
e2.amt()

print(e1.disp())
print(e2.disp())
