from abc import ABC, abstractmethod
class z(ABC):
    @abstractmethod
    def show(self):
        pass
class a(z):
    def show(self):
        print("hello")
class b(a):
    def show1(self):
       print("this is b")

obj=b()
obj.show()
obj.show1()
 