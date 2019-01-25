d={}
class emp:
    def gettar(self):
        self.name=input("Enter the name")
        self.add=input("Enter the add")
        self.pan=int(input("Enter the panno"))
        self.basic=int(input("Enter the baisc"))
        self.hra=1.05*self.basic
        self.da=1.8*self.basic
        self.cca=300
        self.pf=2000
        self.pt=200
        self.tds=int(input("Enter the tds"))
        self.de=int(input("Enter the deduct"))
        self.netsal=self.da+self.basic+self.hra+self.cca-(self.pf+self.pt+self.tds+self.de)
    def dis(self):
        print("name=",self.name)
        print("address=",self.add)
        print("panno=",self.pan)
        print("basic=",self.basic)
        print("hra=",self.hra)
        print("da=",self.da)
        print("cca=",self.cca)
        print("pf=",self.pf)
        print("pt=",self.pt)
        print("tds=",self.tds)
        print("deduct=",self.de)
        print("netsal=",self.netsal)
e=emp()
while True:
    print("1.enter details")
    print("2.displa")
    print("3.update")
    print("4.search")
    ch=int(input("Ente rthe choice"))
    if ch==1:
        e.gettar()
    elif ch==2:
        e.dis()
    elif ch==3:
        d=e.__dict__
        print(d)
    elif ch==4:
        k=input("Enter the key")
        print(d[k])
        
    

