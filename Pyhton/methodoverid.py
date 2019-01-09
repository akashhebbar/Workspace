class a:
    def show(self):
        print("hello")
class b(a):
        def show(self):
            print("this is b")
obj= b()
obj.show()