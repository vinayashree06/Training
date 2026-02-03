class Student:
    def get_role(self):
        print("I am a Student")
class Faculty:
    def get_role(self):
        print("I am a Faculty")
class PhDStudent(Student, Faculty):
    pass
obj = PhDStudent()
obj.get_role()
