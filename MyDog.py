# ❑ Create a class named MyDog and define the following properties.
# ➢ instance attributes: breed, name, age, color, isAsleep=False
# ➢ __init__ method that takes breed, name, age, color as parameters, sets the values
# for them and also sets isAsleep to False
# ➢ instance methods:
# ▶ walk() which prints "name is walking!"
# ▶ eat(food) which prints "name is eating food!"
# ▶ sleep() which changes the value of the instance attribute, isAsleep to True and
# prints "name is sleeping!"
# ▶ wake_up() which changes the value of the instance attribute, isAsleep to False
# and prints "name is waking up!"
# ▶ info() which prints out the values for all instance attributes except isAsleep.
# Create two instances of MyDog class.
# ➢ On the first instance, invoke method walk and then sleep.
# ➢ On the second instance, invoke method eat and then sleep.
# ➢ On the first instance, invoke method wake_up and then eat.
# ➢ Print out the description of the instances using info method.
# ❑ Use the MyDog class created from previous problem.
# class attribute: home_address
# ➢ class method:
# ▶ from_birthyear() which returns cls that allows accepting birthyear instead of age
# as parameter. (*hint – use datetime module)
# ▶ move(destination) which changes value of the class attribute, home_address to
# destination and prints "We moved to destination!!"
# ➢ static method:
# ▶ checkup_needed(age) which returns True if the age is x, such that
# (x - 1) % 3 = 0, False otherwise.
# Print out the description of the instances using info method to make sure the ages
# are calculated correctly.
# ➢ On the first instance, print its home_address.
# ➢ Change the value for home_address using move method.
# ➢ On the second instance, print its home_address and check if the value has been
# properly changed.
# ➢ Check if two instances need checkup using checkup_needed method.

import datetime


class MyDog:
    home_address = "PA"

    def __init__(self, bread, name, age, color):
        self.bread = bread
        self.age = age
        self.name = name
        self.color = color
        self.isAsleep = False

    @staticmethod
    def from_birthyear(birth_year):
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return age

    @classmethod
    def move(cls, destination):
        cls.home_address = destination
        print(f"we moved to {cls.home_address}")

    @classmethod
    def checkup_needed(cls, age):
        return (age - 1) % 3 == 0

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


myDog1 = MyDog("aaa", "tiger", "2", "brown")
myDog2 = MyDog("aaa", "lion", "3", "black")

myDog1.walk()
myDog1.sleep()

myDog2.eat()
myDog2.sleep()

myDog1.wake_up()
myDog1.eat()

myDog1.info()
myDog2.info()

print(MyDog.from_birthyear(2011))
print(myDog1.home_address)
myDog1.move("CA")
print(myDog1.home_address)
print(myDog2.home_address)
print(myDog1.checkup_needed(10))
print(myDog1.checkup_needed(12))
