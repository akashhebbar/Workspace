class parent:
        def show (self):
            print("parent class")
            print("level 1")
class son(parent):
        def disp(self):
            print("son class")
            print("level 2")
class daugher(son):
        def display(self):
            print("daughter class")
            print("level 3")
obj=daugher()
ob2=parent()
obj.show()
obj.display()
ob2.show()
obj.disp()