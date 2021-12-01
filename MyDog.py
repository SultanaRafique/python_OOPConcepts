class MyDod:
    def __init__(self, bread, name, age, color):
        self.bread = bread
        self.age = age
        self.name = name
        self.color = color
        self.isAsleep = False

    def walk(self):
        print(f"{self.name} is walking")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        self.isAsleep = True
        print(f"{self.name} is sleeping")

    def wake_up(self):
        self.isAsleep = False
        print(f"{self.name} is waking up")

    def info(self):
        print(f"Bread: {self.bread}, Age: {self.age}, Name: {self.name}, Color: {self.color}")


myDog1 = MyDod("aaa", "tiger", "2", "brown")
myDog2 = MyDod("aaa", "lion", "3", "black")

myDog1.walk()
myDog1.sleep()

myDog2.eat()
myDog2.sleep()

myDog1.wake_up()
myDog1.eat()

myDog1.info()
myDog2.info()





