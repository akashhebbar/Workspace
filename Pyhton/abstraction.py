from abc import ABC, abstractmethod
class z(ABC):
    @abstractmethod
    def show(self):
        pass
class a(z):
    def show(self):
        print("hello")
class b(a):
    def show(self):
        print("this is b")
obj= b()
obj1=a()
obj1.show()
obj.show()