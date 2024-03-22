class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
        
    def engineStart(self):
        print(self.brand + "열쇠로 시동 킴")
        
    def engineStop(self):
        print(self.brand + "열쇠로 시동 끔")
        
class SuperCar(Car):
    def __init__(self, brand, color, price ,mode):
        super().__init__(brand, color, price)
        self.mode =mode
        
    def engineStart(self):
        print(self.brand + "음성으로 시동 킴")
        
    def openRoot(self):
        print("지붕 열림")
        
    def closeRoof(self):
        print("지붕 닫힘")
        
        
ferrari = SuperCar("ferrari","red",35000,"daily")

ferrari.engineStart()
ferrari.engineStop()
ferrari.openRoot()
ferrari.closeRoof()

class A:
    # 모든 객체가 공용으로 사용한다.
    seq = 0
    
    def __init__(self):
        A.seq += 1
        self.num = A.seq
        
    def test(self):
        self.seq =10
        
        
obj1= A()
obj2= A()
obj3= A()
obj4= A()