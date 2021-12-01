class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name


class Student(Person):
    def __init__(self, f_name, l_name, course, enrolled):
        self.course = course
        self.enrolled = enrolled
        self.graduated = False
        super().__init__(f_name, l_name)


s = Student("f-name", "l-name", "course", "enrolled_true")
print(f"{s.f_name}, {s.l_name}, {s.course}, {s.enrolled}")