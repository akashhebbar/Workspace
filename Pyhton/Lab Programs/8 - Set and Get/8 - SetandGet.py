class Employee(object):
   
    #Magic method - setattr to Set the attribute for the class
    def __setattr__(self, name, value):
        #print(name)
        if name=="empno" or name=="empname" or name=="designation" or name=="empstatus":
            self.__dict__[name] = value
            print("value set for %s -- %s"%(name,value))
        else:
            print("cannot set '%s' attributes other than - empno,empname,designation,empstatus"%(name))
            return 0
           
    #Magic method - getattr to get the attribute for the class
    def __getattr__(self, name):
        # we don't need a special call to super here because getattr is only
        # called when an attribute is NOT found in the instance's dictionary
        try:
            if not(name=="empno" or name=="empname" or name=="designation" or name=="empstatus"):
                return "Attribute not found -- %s"%(name)
        except KeyError:
            raise AttributeError

e = Employee()       

print("attributes should be same as in list - empno,empname,designation,empstatus")
lp = True
while(lp):
    a = input("enter the attribute name:")
    v = input("enter the attribute value:")
    valuestatus=setattr(e, a, v)
    if(valuestatus==0):
        print("attribute not added")
    if input("do u want to continue:y/n - ")=='n':
        break
print("List of attributes are added")
print(e.__dict__)
