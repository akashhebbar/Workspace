from abc import ABC,abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def talk(self):
         pass

  

class Duck(AbstractAnimal):

    def __init__(self, name):       
        self.name = name
        print('duck created.')

    def walk(self):
        print('walks')

    def talk(self):
        print('quack')

obj = Duck('duck1')

obj.talk()
obj.walk()