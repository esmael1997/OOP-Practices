class Computer :
    count = 0
    def __init__(self,ram,hard,cpu):
        Computer.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
        
    def value(self):
        return self.ram + self.hard + self.cpu
    
    def __del__(self):
        Computer.count -= 5
        
class laptop(Computer):
    def value(self):
        return self.ram + self.hard + self.cpu + self.size
    
pc1 = Computer(13,4,5)

print(pc1.value())

del pc1


laptop1 = laptop(4,6,5)

laptop.size = 12

print(laptop1.value())
       


            