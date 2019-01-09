class MyClass: 
  
   
    __hidden = 0
    
     
    def add(self, increment): 
        self.__hidden += increment 
        print (self.__hidden) 
        
# Driver code 
myObject = MyClass()      
myObject.add(1) 
myObject.add(5) 
  
# This line causes error 
print (myObject.__hidden) 