from abc import ABC,abstractmethod

class Main(ABC):
    def GUN(self):
        print("AK-74")
    
    @abstractmethod
    def Area(self):
        pass

class Army(Main):
    def Area(self):
        print("On Land")
        
class AirForce(Main):
    def Area(self):
        print("On Sky")

class Navy(Main):
    def Area(self):
        print("On Sea")
        
a = Army()
af = AirForce()
n = Navy()

a.GUN()
a.Area()

af.GUN()
af.Area()

n.GUN()
n.Area()                            