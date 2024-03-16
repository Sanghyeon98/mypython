#class Test
class A:
    data = 10
    
    def printData(self):
        print(self)
        print(self.data)
        
    def intro():
        print("난 A클래스 이다.")
        
obj1 = A()
obj2 = A()

obj1.data =20
print(obj1)
obj1.printData()
print(obj2)
obj2.printData()
A.intro()

#class test2
class Car:
    brand = ""
    color=""
    price=""
    
    
    
    def __init__(self, brand="",color="", price=0):
        self.brand =brand
        self.color =color
        self.brand=brand
        
    
    def engineStart(self):
        print(self.brand+"시동 킴")
        
    def engineStop(self):
        print(self.brand +"시동 끔")
    
momCar =Car("벤츠","검정색",15000)

print(momCar)