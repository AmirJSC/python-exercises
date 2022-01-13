class Robot:
    def __init__(self, name, color, weight):#This is a constructor
        self.name = name
        self.color = color
        self.weight = weight
        
    def introduce_self(self):
        print('My name is ' + self.name)

class Person:
    def __init__(self, name, personality, isSitting): #A constructor for a person
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sitDown(self):
        self.isSitting = True
        
    def standUp(self):
        self.isSitting = False
        
r1 = Robot('tom','red',30)
r2 = Robot('jerry','blue',40)


p1 = Person('Alice','aggressive', False)
p2 = Person('Becky','talkative',True)
p1.robotOwned = r2
p2.robotOwned = r1

p1.robotOwned.introduce_self()
p2.robotOwned.introduce_self()

