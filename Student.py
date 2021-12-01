import pprint


class Student:
    school_name = "PerScholas"

    def __init__(self, student_id, name, address):
        self.student_id = student_id
        self.name = name
        self.address = address

    @property
    def all_info(self):
        return f"id: {s.student_id}, name: {s.name}, address: {s.address}"

    @classmethod
    def from_info(cls, info):
        student_id, name, address = info.split(',')
        return cls(student_id, name, address)

    @staticmethod
    def print_msg():
        print("hello student")

s = Student(111, "aaa", "PA")
s1 = Student(222, "bbb", "CA")
print(f"id: {s.student_id}, name: {s.name}, address: {s.address}")
s.email = "aa.ddd@asd.com"
print(s.email)
print(Student.school_name)
print(hasattr(s1, "email"))
print((hasattr(s1, "student_id")))
setattr(s1, "name", "jjjj")
print(s1.name)
# print(s1.all_info())
print(s1.all_info)
s3 = Student.from_info('9999, jjj, CA')
print(f"id: {s3.student_id}, name: {s3.name}, address: {s3.address}")
s1.print_msg()
Student.print_msg()
print(dir(s1))
print(dir(s3))
pprint.pprint(vars(s3))