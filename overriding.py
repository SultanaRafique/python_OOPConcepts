class Person:
    def introduce(self):
        print("Person")

    def sleep(self):
        print("person sleeping")


class Student(Person):
    def introduce(self):
        print("Student")

s = Student()
s.introduce()
s.sleep()